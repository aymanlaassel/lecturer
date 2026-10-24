#!/usr/bin/env python3
"""
Ingest course materials (PDF, PPTX, DOCX, XLSX, TXT, MD) into plain markdown
so Claude can read and search them.

Usage:
    python3 scripts/ingest.py courses/<course>            # ingest everything in <course>/inbox
    python3 scripts/ingest.py courses/<course> file.pdf   # ingest specific files
    python3 scripts/ingest.py courses/<course> --force    # re-extract even if up to date

Output: courses/<course>/extracted/<original-name>.md
Also writes courses/<course>/extracted/INDEX.md listing every source with a size and
first-heading preview, which CLAUDE.md tells Claude to read first.
"""
import sys, os, re, json, warnings, shutil, hashlib
from pathlib import Path
from datetime import datetime

warnings.filterwarnings("ignore")

SUPPORTED = {".pdf", ".pptx", ".docx", ".xlsx", ".txt", ".md", ".csv"}


def extract_pdf(path: Path) -> str:
    import pymupdf
    out = []
    with pymupdf.open(path) as doc:
        for i, page in enumerate(doc, 1):
            text = page.get_text("text").strip()
            out.append(f"\n\n---\n## Page {i}\n\n{text}")
    return "".join(out)


def extract_pptx(path: Path) -> str:
    from pptx import Presentation
    from pptx.util import Emu
    prs = Presentation(path)
    out = []
    for i, slide in enumerate(prs.slides, 1):
        title = None
        if slide.shapes.title is not None and slide.shapes.title.has_text_frame:
            title = slide.shapes.title.text_frame.text.strip()
        out.append(f"\n\n---\n## Slide {i}" + (f": {title}" if title else ""))
        # sort shapes top-to-bottom, left-to-right for reading order
        shapes = sorted(slide.shapes, key=lambda s: ((s.top or 0), (s.left or 0)))
        for shape in shapes:
            if shape == slide.shapes.title:
                continue
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    t = "".join(r.text for r in para.runs).strip()
                    if t:
                        indent = "  " * (para.level or 0)
                        out.append(f"\n{indent}- {t}")
            if getattr(shape, "has_table", False) and shape.has_table:
                tbl = shape.table
                rows = [[c.text.strip().replace("\n", " ") for c in r.cells] for r in tbl.rows]
                if rows:
                    out.append("\n\n| " + " | ".join(rows[0]) + " |")
                    out.append("\n|" + "---|" * len(rows[0]))
                    for r in rows[1:]:
                        out.append("\n| " + " | ".join(r) + " |")
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text.strip()
            if notes:
                out.append(f"\n\n> **Speaker notes:** {notes}")
    return "".join(out)


def extract_docx(path: Path) -> str:
    import docx
    d = docx.Document(path)
    out = []
    for block in d.element.body.iterchildren():
        tag = block.tag.split("}")[-1]
        if tag == "p":
            p = docx.text.paragraph.Paragraph(block, d)
            t = p.text.strip()
            if not t:
                continue
            style = (p.style.name or "").lower()
            m = re.match(r"heading (\d)", style)
            if m:
                out.append("\n\n" + "#" * (int(m.group(1)) + 1) + " " + t)
            elif "list" in style:
                out.append("\n- " + t)
            else:
                out.append("\n\n" + t)
        elif tag == "tbl":
            t = docx.table.Table(block, d)
            rows = [[c.text.strip().replace("\n", " ") for c in r.cells] for r in t.rows]
            if rows:
                out.append("\n\n| " + " | ".join(rows[0]) + " |")
                out.append("\n|" + "---|" * len(rows[0]))
                for r in rows[1:]:
                    out.append("\n| " + " | ".join(r) + " |")
    return "".join(out)


def extract_xlsx(path: Path) -> str:
    import openpyxl
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    out = []
    for ws in wb.worksheets:
        out.append(f"\n\n## Sheet: {ws.title}\n")
        for row in ws.iter_rows(values_only=True):
            if any(v is not None for v in row):
                out.append("| " + " | ".join("" if v is None else str(v) for v in row) + " |\n")
    return "".join(out)


def extract_text(path: Path) -> str:
    return path.read_text(errors="replace")


EXTRACTORS = {
    ".pdf": extract_pdf,
    ".pptx": extract_pptx,
    ".docx": extract_docx,
    ".xlsx": extract_xlsx,
    ".txt": extract_text,
    ".md": extract_text,
    ".csv": extract_text,
}


def file_hash(p: Path) -> str:
    h = hashlib.sha1()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def slug(name: str) -> str:
    s = re.sub(r"[^\w.\- ]+", "", name).strip().replace(" ", "_")
    return s or "file"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(1)
    course = Path(args[0]).resolve()
    inbox = course / "inbox"
    extracted = course / "extracted"
    extracted.mkdir(parents=True, exist_ok=True)
    inbox.mkdir(parents=True, exist_ok=True)

    manifest_path = extracted / ".manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}

    if len(args) > 1:
        sources = [Path(a).resolve() for a in args[1:]]
    else:
        sources = sorted(p for p in inbox.rglob("*") if p.is_file() and not p.name.startswith("."))

    done, skipped, failed = [], [], []
    for src in sources:
        ext = src.suffix.lower()
        if ext not in SUPPORTED:
            skipped.append((src.name, "unsupported type"))
            continue
        # if given a file outside inbox, copy it into inbox so it is kept
        if inbox not in src.parents:
            dest = inbox / src.name
            if not dest.exists():
                shutil.copy2(src, dest)
            src = dest
        h = file_hash(src)
        out_path = extracted / (slug(src.stem) + ext.replace(".", "_") + ".md")
        if not force and manifest.get(src.name, {}).get("hash") == h and out_path.exists():
            skipped.append((src.name, "up to date"))
            continue
        try:
            body = EXTRACTORS[ext](src)
        except Exception as e:  # keep going on bad files
            failed.append((src.name, repr(e)))
            continue
        body = re.sub(r"\n{4,}", "\n\n\n", body).strip()
        words = len(body.split())
        header = (
            f"# {src.name}\n\n"
            f"> Source: `inbox/{src.relative_to(inbox)}` · type: {ext[1:]} · "
            f"~{words} words · extracted {datetime.now():%Y-%m-%d %H:%M}\n\n"
        )
        out_path.write_text(header + body + "\n")
        manifest[src.name] = {"hash": h, "out": out_path.name, "words": words,
                              "ingested": datetime.now().isoformat(timespec="seconds")}
        done.append((src.name, out_path.name, words))

    manifest_path.write_text(json.dumps(manifest, indent=2))

    # Rebuild INDEX.md
    lines = [f"# Extracted materials index — {course.name}\n",
             f"_Rebuilt {datetime.now():%Y-%m-%d %H:%M}. Read the files below from `extracted/`._\n",
             "| Source file | Extracted markdown | Words | Preview |", "|---|---|---|---|"]
    for name, info in sorted(manifest.items()):
        p = extracted / info["out"]
        preview = ""
        if p.exists():
            for line in p.read_text().splitlines()[3:]:
                line = line.strip().lstrip("#-> ").strip()
                if len(line) > 25 and not line.startswith("Page ") and not line.startswith("Slide "):
                    preview = line[:90].replace("|", "/")
                    break
        lines.append(f"| {name} | `{info['out']}` | {info['words']} | {preview} |")
    (extracted / "INDEX.md").write_text("\n".join(lines) + "\n")

    for n, o, w in done:
        print(f"  ✓ {n}  →  extracted/{o}  ({w} words)")
    for n, why in skipped:
        print(f"  – {n}  ({why})")
    for n, why in failed:
        print(f"  ✗ {n}  FAILED: {why}")
    print(f"\n{len(done)} extracted, {len(skipped)} skipped, {len(failed)} failed. Index: {extracted/'INDEX.md'}")


if __name__ == "__main__":
    main()
