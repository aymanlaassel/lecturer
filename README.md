# Lecturer

An AI tutor plugin for [Claude Code](https://claude.com/claude-code). Drop your slides,
PDFs, readings and past quizzes into a folder, and Claude teaches you, quizzes you, and
writes review sheets **from your own course materials**, citing the slide or section each
fact came from.

## Install (2 minutes)

You need [Claude Code](https://code.claude.com/docs/en/quickstart) and Python 3.10+.

**1. Install the plugin.** In your terminal:

```bash
claude plugin install lecturer --marketplace aymanlaassel/lecturer
```

(On Claude Code older than 2.1.292, run these two instead:
`claude plugin marketplace add aymanlaassel/lecturer` then `claude plugin install lecturer@lecturer`.)

**2. Install the file readers** (PDF, PowerPoint, Word, Excel):

```bash
pip3 install pymupdf python-docx python-pptx openpyxl
```

If you skip this, the plugin will offer to install them the first time it needs them.

**3. Make a study folder and start Claude in it:**

```bash
mkdir -p ~/Study && cd ~/Study
claude
```

## Use it

Inside Claude Code, paste your professor's exam email or syllabus and run:

```
/lecturer:setup logic-cs   <paste the exam email / syllabus here>
```

That creates `courses/logic-cs/` with a filled-in `COURSE.md` and an `inbox/` folder.
Drop your files into `courses/logic-cs/inbox/` (Finder: `open courses/logic-cs/inbox`), then:

| Command | What it does |
|---|---|
| `/lecturer:ingest` | Read everything new in `inbox/` and mark which topics are now covered |
| `/lecturer:exam-info` | When, where, format, what to bring, days left, which topics still lack files |
| `/lecturer:teach 5` | Full lesson on Module 5, saved to `notes/05-*.md` |
| `/lecturer:teach all` | One lesson per module plus an overview |
| `/lecturer:explain sound vs complete` | Short targeted explanation, or paste a question to solve |
| `/lecturer:quiz 3 4 10` | 10 practice questions on Modules 3 and 4, graded with explanations |
| `/lecturer:quiz all 18` | Full mock exam in the real format |
| `/lecturer:cheatsheet` | Two-page last-minute review sheet |

You can also just talk: *"teach me everything I need to remember from module 7"*.

Multiple courses? Run `/lecturer:setup <name>` for each one and name the course in commands,
e.g. `/lecturer:teach calc2 3`.

## What goes where

```
~/Study/                      your folder, anywhere you like
  courses/<course>/
    COURSE.md                 exam info and topic list
    inbox/                    raw files you drop in (pdf, pptx, docx, xlsx, txt, md, csv)
    extracted/                searchable markdown the plugin makes from inbox/
    notes/                    lessons it writes
    quizzes/                  quizzes it writes, plus log.md of your scores
```

Your files never leave your machine except as context sent to Claude when you ask it to teach.

## Update

```bash
claude plugin update lecturer@lecturer
```

## Tips

- The **mock exam / practice questions with solutions** is the most valuable file to add first.
  Quizzes mirror its style.
- Scanned PDFs with no text layer extract to almost nothing. The ingest step flags them and
  Claude can read those pages as images instead.
- To check extraction without Claude:
  `python3 ~/.claude/plugins/cache/lecturer/lecturer/*/scripts/ingest.py courses/<course>`

## Develop

```bash
git clone https://github.com/aymanlaassel/lecturer.git
cd lecturer
claude plugin validate .
claude --plugin-dir .          # load this checkout for one session
```

Skills live in `skills/*/SKILL.md`, the tutor rules in `rules/TUTOR.md`, extraction in
`scripts/ingest.py`.

## License

MIT
