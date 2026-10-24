---
name: quiz
description: Generate and grade a practice quiz in the exam's style (multiple choice + true/false, shuffled answers) from the course materials, and log results to track weak topics. Use for "quiz me", "test me on module 3", "give me 18 mock questions", "practice exam".
---

Arguments: `$ARGUMENTS` = module number(s) or "all", optionally a question count.
Defaults: all modules, 10 questions (use 18 for a "mock midterm"). Default course `logic-cs`.

1. Read `COURSE.md`, `extracted/INDEX.md`, the relevant `extracted/*.md`, and the tail of
   `courses/<course>/quizzes/log.md` if it exists (weight weak topics more heavily).
2. Build questions that imitate the real exam:
   - Mix of MC (4 options) and T/F, roughly 50/50 slides-based vs zyBooks-based when both exist.
   - Mirror the style of any mock midterm / past quiz in the materials.
   - Favor computation-with-a-definite-answer (e.g. "which formula is the CNF of…",
     "the contrapositive of p→¬q is…", "how many rows does the truth table have") and
     precise-definition traps (sound/complete, valid/satisfiable, tautology/contingency).
   - Exactly one correct answer; distractors should be the classic mistakes.
3. Present ALL questions at once with no answers (the student is simulating a timed exam),
   numbered, and say "reply with your answers like `1A 2T 3C …`".
4. When the student replies, grade: score, per-question ✓/✗, and for every wrong (or
   skipped) one a 2–4 line explanation with a citation to the slide / zyBooks section.
5. Save the quiz + key to `courses/<course>/quizzes/<YYYY-MM-DD>-<scope>-<n>.md` and append
   a line to `quizzes/log.md`: `date | scope | score | topics missed`.
6. Finish with the 1–3 topics to review next and offer `/teach <topic>` or `/explain`.
