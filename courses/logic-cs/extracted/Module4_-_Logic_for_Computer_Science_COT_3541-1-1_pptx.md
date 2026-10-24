# Module4 - Logic for Computer Science COT 3541-1-1.pptx

> Source: `inbox/Module4 - Logic for Computer Science COT 3541-1-1.pptx` · type: pptx · ~904 words · extracted 2026-10-24 13:00

---
## Slide 1: Logic for Computer ScienceCOT 3541
- Kiavash Bahreini, Ph.D.
- Associate Teaching Professor
- Knight Foundation School of Computing and Information Sciences (KFSCIS)
- School of computing and information sciences (SCIS)
- Florida international university (FIU)
- Module 4

---
## Slide 2: Content
- Tautologies
- Contradictions
- Contingency
- More examples
  - Propositional equivalences

---
## Slide 3: Tautologies
- Definition: A tautology is an always TRUE formula:
  - For every value of its propositional variables
- Task 1. prove that the following formula will be always TRUE for every value of its propositional variables:
  - [(P → Q) ∧ P] → Q
- Solution 1: We will use a truth table.

| P | Q | P → Q | (P → Q) ∧ P | [( P → Q ) ∧ P] → Q |
|---|---|---|---|---|
| TRUE | TRUE | TRUE | TRUE | TRUE |
| TRUE | FALSE | FALSE | FALSE | TRUE |
| FALSE | TRUE | TRUE | FALSE | TRUE |
| FALSE | FALSE | TRUE | FALSE | TRUE |
  - It is clear that every value of [(P → Q) ∧ P] → Q is always TRUE. Therefore, this formula is a tautology.

---
## Slide 4: Contradictions
- Definition: A contradiction is an always FALSE formula:
  - For every value of its propositional variables
- Task 2. prove that the following formula will be always FALSE for every value of its propositional variables:
  - (P ∨ Q) ∧ [(¬P) ∧ (¬Q)]
- Solution 2: We will use a truth table.

| P | Q | P ∨ Q | ¬P | ¬Q | (¬P) ∧ ( ¬Q) | (P ∨ Q) ∧ [( ¬P) ∧ (¬Q)] |
|---|---|---|---|---|---|---|
| TRUE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE |
| TRUE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE |
| FALSE | TRUE | TRUE | TRUE | FALSE | FALSE | FALSE |
| FALSE | FALSE | FALSE | TRUE | TRUE | TRUE | FALSE |
  - It is clear that every value of (P ∨ Q) ∧ [(¬P) ∧ (¬Q)] is always FALSE. Therefore, this formula is a contradiction.

---
## Slide 5: Contingency
- Definition: A contingency is a TRUE and FALSE formula:
  - For every value of its propositional variables
- Task 3. prove that the following formula will be TRUE and FALSE for every value of its propositional variables:
  - (P ∨ Q) ∧ (¬P)
- Solution 3: We will use a truth table.

| P | Q | P ∨ Q | ¬P | (P ∨ Q) ∧ (¬P) |
|---|---|---|---|---|
| TRUE | TRUE | TRUE | FALSE | FALSE |
| TRUE | FALSE | TRUE | FALSE | FALSE |
| FALSE | TRUE | TRUE | TRUE | TRUE |
| FALSE | FALSE | FALSE | TRUE | FALSE |
  - It is clear that every value of (P ∨ Q) ∧ (¬P) has both TRUE and FALSE. Therefore, this formula is a contingency.

---
## Slide 6: Propositional equivalences
- Definition: Two statements, P and Q, are logically equivalent if one of the following conditions occurs:
- The truth tables of each statement have the same truth values.
- The biconditional statement P ⇔ Q is a tautology.

---
## Slide 7: Propositional equivalences
- Task 4: Prove that ¬(P ∨ Q) and [(¬P) ∧ (¬Q)] are equal
- Solution 4.1: We will use two truth tables. First, we test the matching truth table.

| P | Q | P ∨ Q | ¬(P ∨ Q) | ¬P | ¬Q | [(¬P) ∧ (¬Q)] |
|---|---|---|---|---|---|---|
| TRUE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE |
| TRUE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE |
| FALSE | TRUE | TRUE | FALSE | TRUE | FALSE | FALSE |
| FALSE | FALSE | FALSE | TRUE | TRUE | TRUE | TRUE |
  - It is clear that the truth values of ¬(P ∨ Q) and [(¬P) ∧ (¬Q)] are the same. Therefore, the statements are equal.

---
## Slide 8: Propositional equivalences
- Task 4: Prove that ¬(P ∨ Q) and [(¬P) ∧ (¬Q)] are equal
- Solution 4.2: We will use two truth tables. Second, we test the biconditionality truth table.

| P | Q | P ∨ Q | ¬(P ∨ Q) | ¬P | ¬Q | [(¬P) ∧ (¬Q)] | [¬ (P ∨ Q)] ⇔ [(¬ P ) ∧ (¬ Q)] |
|---|---|---|---|---|---|---|---|
| TRUE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE |
| TRUE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | TRUE |
| FALSE | TRUE | TRUE | FALSE | TRUE | FALSE | FALSE | TRUE |
| FALSE | FALSE | FALSE | TRUE | TRUE | TRUE | TRUE | TRUE |
  - It is clear that ¬(P ∨ Q) and [(¬P) ∧ (¬Q)] is a tautology. Therefore, the statements are equal.

---
## Slide 9: Tasks
- Study all modules
- Read the pdf chapters shared with you
- Read the lecture notes
- Watch the lecture video files
- Solve the assignments
