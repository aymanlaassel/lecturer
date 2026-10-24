---
name: teach
description: Deliver a full exam-focused lesson on a module or topic, grounded in the ingested course materials, and save it to notes/. Use for "teach me module 5", "teach me everything about resolution", "walk me through tableaux", "teach me everything I need for the exam".
---

Read `${CLAUDE_PLUGIN_ROOT}/rules/TUTOR.md` first and follow its course-resolution and ingest rules.
Arguments: `$ARGUMENTS` = module number, topic name, or "all". 

1. Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/ingest.py" courses/<course>` (incremental) then read
   `courses/<course>/COURSE.md` and `courses/<course>/extracted/INDEX.md`.
2. Identify the extracted files relevant to the requested topic (match module numbers,
   titles, keywords). Read them fully. If nothing matches, say so and teach from your own
   knowledge, marking the lesson `⚠ not from course materials`.
3. Write the lesson following the **Structure of a lesson** in TUTOR.md:
   context → definitions (professor's wording) → worked examples from the materials →
   exam traps → quick-check questions with hidden answers.
   - Keep the professor's notation. Quote slide numbers / zyBooks section numbers.
   - For procedures (truth tables, CNF conversion, resolution, tableaux, Hilbert proofs)
     show every intermediate step once, slowly, then a second example compactly.
   - Call out anything the mock midterm or past quizzes tested on this topic.
4. Save to `courses/<course>/notes/<NN>-<slug>.md` (NN = module number, `00` for
   cross-cutting topics). If "all" was requested, produce one file per module and finish
   with a short "how the modules connect" overview in `notes/00-overview.md`.
5. End the reply with the saved path(s) and offer `/lecturer:quiz <module>` as the next step.
