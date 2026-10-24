---
name: setup
description: Create a new course folder (COURSE.md + inbox/) in the current directory and fill in exam details from whatever the student pastes (syllabus, professor's email, Canvas page). Use for "set up a course", "new course", "here is the exam email", or when no courses/ folder exists yet.
---

Read `${CLAUDE_PLUGIN_ROOT}/rules/TUTOR.md` first.

Arguments: `$ARGUMENTS` = a short kebab-case course name (e.g. `logic-cs`, `calc2`,
`organic-chem`) optionally followed by pasted exam information.

1. If no name was given, derive one from the pasted text (course subject + exam), confirm it in
   one line, and proceed.
2. Create `courses/<name>/{inbox,extracted,notes,quizzes}` in the current directory.
3. Copy `${CLAUDE_PLUGIN_ROOT}/templates/COURSE.md` to `courses/<name>/COURSE.md` and fill in
   every field you can from the pasted text: dates, room, time limit, rules, format, question
   split, the full topic list as table rows, listed study resources, nearby deadlines.
   Leave `<placeholders>` for anything unknown. See
   `${CLAUDE_PLUGIN_ROOT}/examples/COURSE.logic-cs.md` for what a finished one looks like.
4. Check that the Python extraction libraries import
   (`python3 -c "import pymupdf, docx, pptx, openpyxl"`); if not, install them per TUTOR.md.
5. Reply with: the folder path, the exam date and days remaining, what to drop into
   `courses/<name>/inbox/`, and the next command (`/lecturer:ingest <name>`).
