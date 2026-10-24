---
name: ingest
description: Extract course materials (pdf, pptx, docx, xlsx, txt, md) from courses/<course>/inbox into searchable markdown. Use when the student adds new files or says "ingest", "add these slides", "load the materials".
---

Arguments: `$ARGUMENTS` = optional course name, then optional file paths.
Default course: `logic-cs`.

Steps:
1. If the student attached or named files that are not yet in `courses/<course>/inbox/`,
   pass their paths to the script; it copies them into inbox.
   `python3 scripts/ingest.py courses/<course> <paths...>`
   Otherwise just run `python3 scripts/ingest.py courses/<course>`.
2. Show the script's summary (extracted / skipped / failed).
3. Open `courses/<course>/extracted/INDEX.md`. Skim each newly extracted file and decide
   which module(s) of `COURSE.md` it covers. Update the **Status of materials** column in
   `COURSE.md` (e.g. `slides ✓`, `zyBooks ✓`, `mock exam ✓`).
4. If a PDF extracted to almost no text (scanned images), tell the student and offer to
   read it page-by-page with the Read tool (which can view PDF pages as images).
5. Report in 3–6 lines: what was added, which modules now have coverage, which modules
   are still missing materials.
