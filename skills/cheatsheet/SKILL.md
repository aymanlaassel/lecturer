---
name: cheatsheet
description: Produce a dense one-to-two page review sheet covering every module of the course — definitions, equivalence laws, procedures, and traps — for last-minute revision. Use for "cheat sheet", "summary of everything", "one-pager", "what do I need to memorize".
---

Read `${CLAUDE_PLUGIN_ROOT}/rules/TUTOR.md` first and follow its course-resolution and ingest rules.
1. Read `COURSE.md`, `extracted/INDEX.md`, and every lesson in `notes/` (generate missing
   module lessons with the `/lecturer:teach` procedure first only if the student asks; otherwise
   draw directly from `extracted/`).
2. Write `courses/<course>/CHEATSHEET.md` with one compact section per module:
   - Definitions in the professor's wording (1 line each)
   - Tables where they help (connective truth table, equivalence laws with names,
     inference rules, tableau α/β rules, Hilbert axioms)
   - Procedure checklists (numbered, ≤6 steps each)
   - "Don't confuse" pairs
3. Keep it to roughly what fits on two printed pages. No prose paragraphs; bullets and tables.
4. Reply with the path and the three most-tested facts to re-read right before the exam.
