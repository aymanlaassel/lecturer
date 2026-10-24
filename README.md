# Lecturer

Personal AI tutor that runs inside [Claude Code](https://claude.com/claude-code). Drop your
slides, PDFs, readings and past quizzes into a course folder and ask it to teach you, quiz
you, or summarize, grounded in **your** course materials with citations to the slide or
section they came from.

## How it works

```
courses/<course>/
  COURSE.md      exam date, format, topics, professor's instructions
  inbox/         raw files you drop in (pdf, pptx, docx, xlsx, txt, md, csv)
  extracted/     markdown produced by scripts/ingest.py (+ INDEX.md)
  notes/         lessons the tutor writes
  quizzes/       practice quizzes and your results log
scripts/ingest.py   converts inbox/* into extracted/*.md (incremental)
CLAUDE.md           the tutor persona and rules
.claude/skills/     the slash commands below
```

## Setup

```bash
git clone https://github.com/aymanlaassel/lecturer.git
cd lecturer
pip3 install -r requirements.txt       # pymupdf python-docx python-pptx openpyxl
```

Requires Python 3.10+ and Claude Code installed (`npm install -g @anthropic-ai/claude-code`).

## Run it

```bash
cd lecturer

# 1. drop your materials into the course inbox
open courses/logic-cs/inbox          # macOS; or copy files there manually

# 2. (optional) extract outside Claude to check everything parses
python3 scripts/ingest.py courses/logic-cs
python3 scripts/ingest.py courses/logic-cs --force      # re-extract everything
python3 scripts/ingest.py courses/logic-cs ~/Downloads/Module7.pptx   # add specific files

# 3. start Claude Code in this folder
claude
```

Inside Claude Code:

| Command | What it does |
|---|---|
| `/ingest` | Extract everything new in `inbox/`, update topic coverage in `COURSE.md` |
| `/exam-info` | When, where, format, what to bring, which topics still lack materials |
| `/teach 5` | Full lesson on Module 5, saved to `notes/05-*.md` |
| `/teach all` | One lesson per module plus an overview |
| `/explain sound vs complete` | Short targeted explanation (or paste a question to solve) |
| `/quiz 3 4 10` | 10 practice questions on Modules 3 and 4, graded with explanations |
| `/quiz all 18` | Full mock exam in the real format |
| `/cheatsheet` | Two-page last-minute review sheet at `courses/<course>/CHEATSHEET.md` |

You can also just talk to it: *"teach me everything I need to remember from module 7"*.

## Adding a new course

```bash
mkdir -p courses/<name>/inbox
cp courses/logic-cs/COURSE.md courses/<name>/COURSE.md   # edit exam info + topic list
# drop files into courses/<name>/inbox, then in Claude:
/ingest <name>
/teach <name> all
```

## Notes

- `inbox/` contents and the extraction manifest are gitignored, so course files stay local.
- Scanned PDFs with no text layer extract to almost nothing; the `/ingest` skill will flag
  them and Claude can read those pages as images instead.
