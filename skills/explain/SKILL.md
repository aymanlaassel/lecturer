---
name: explain
description: Short, targeted explanation of a single concept or a single question the student is stuck on, using the course's own definitions. Use for "what's the difference between sound and complete", "why is this CNF", "explain this slide", "is this a tautology".
---

Read `${CLAUDE_PLUGIN_ROOT}/rules/TUTOR.md` first and follow its course-resolution and ingest rules.
Arguments: `$ARGUMENTS` = the concept or question. 

1. Grep `courses/<course>/extracted/` for the key terms before answering. Use the
   professor's definition if found and cite it; otherwise say it is not in the materials.
2. Answer in under ~250 words unless the student asks for depth:
   plain-language idea → formal definition → one tiny example → the one trap an MCQ
   would use against them.
3. If the student pasted a question with answer choices, work it out step by step, state
   the answer, and explain why each wrong choice is wrong.
4. Do not save a file unless asked; `/lecturer:teach` is for saved lessons.
