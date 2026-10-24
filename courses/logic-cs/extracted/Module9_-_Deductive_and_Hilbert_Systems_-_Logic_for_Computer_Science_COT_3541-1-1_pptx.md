# Module9 - Deductive and Hilbert Systems - Logic for Computer Science COT 3541-1-1.pptx

> Source: `inbox/Module9 - Deductive and Hilbert Systems - Logic for Computer Science COT 3541-1-1.pptx` · type: pptx · ~1100 words · extracted 2026-10-24 13:00

---
## Slide 1: Logic for Computer ScienceCOT 3541
- Kiavash Bahreini, Ph.D.
- Associate Teaching Professor
- Knight Foundation School of Computing and Information Sciences (KFSCIS)
- School of computing and information sciences (SCIS)
- Florida international university (FIU)
- Module 9

---
## Slide 2: Content
- Deductive systems
  - Deductive reasoning
- Hilbert system H
- Theorems for other operators
- Exercises

---
## Slide 3: Deductive systems
- The concept of deducing theorems from a set of axioms and rules of inference is ancient.
- It is familiar to every high-school student who has studied Euclidean geometry.
- Modern mathematics is expressed in a style of reasoning that is not far removed from the reasoning used by Greek mathematicians.
- This style can be characterized as ‘formalized informal reasoning.’
- The deductive systems we present in this presentation were developed to formalize mathematical reasoning.

---
## Slide 4: Deductive reasoning
- Deductive reasoning is a type of reasoning that starts with a general premise and applies it to a specific instance.
- For example:
  - All dogs have ears; Pomeranians are dogs; therefore, they have ears.
- Deductive reasoning is also known as "top-down reasoning.”

---
## Slide 5: Deductive reasoning
- Other examples:
  - "All bachelors are unmarried men. John is an unmarried man. Therefore, John is a bachelor".
  - "All dogs have four legs, John's pet is a dog; therefore John's pet has four legs".
  - "All racing cars must go over 80MPH; the Dodge Charger is a racing car, therefore it can go over 80MPH".
  - "Christmas is always Dec. 25th; today is Dec. 25th, therefore it's Christmas".

---
## Slide 6: Why deductive proofs?
- Let U = {A1, . . . , An}. Theorem 2.50 of the textbook showed that U |= A (U validates A) if and only if |= A1 ∧ · · · ∧ An → A (A1 and A2 and An implies A is true). Therefore, if U is a set of axioms, we can use the completeness of the method of semantic tableaux to determine if A follows from U (see Section 2.5.4 of the textbook for precise definitions).
- Why would we want to search for a mathematical proof when we can easily compute if a formula is valid?
- Because there are several problems with a purely semantical approach.

---
## Slide 7: Why deductive proofs?
- The set of axioms may be infinite.
- Very few logics have decision procedures like propositional logic.
- A decision procedure may not give insight into the relationship between the axioms and the theorem.
- A decision procedure produces a ‘yes/no’ answer, so it is difficult to recognize intermediate results (lemmas).

---
## Slide 8: Hilbert system H
- It is a formalization of step-by-step proofs in mathematics.
- It contains a set of three axioms and one rule of inference.
- proofs are constructed as a sequence of formulas:
  - each of which is either an axiom
  - or a formula that has been previously proved
  - or a derivation of a formula from previous formulas in the sequence using the rule of inference

---
## Slide 9: Hilbert system H
- Notation: Capital letters A, B, C, . . . represent arbitrary formulas in propositional logic.
- For example:
  - The notation ⊢A→A means that for any formula A of propositional logic, the formula A→A can be proved.

---
## Slide 10: Hilbert system H
- Definition 3.9 (Deductive system H ) The axioms of H are:
- Axiom 1 ⊢ (A→(B→A)),
- Axiom 2 ⊢ (A→(B→C))→((A→B)→(A→C)),
- Axiom 3 ⊢ (¬B→¬A)→(A→B).
- The rule of inference is modus ponens (MP for short):
- In words, the formula B can be inferred from A and A→B.
- The terminology used for H are premises, conclusion, theorem, proved, and symbol ⊢ (turnstile), meaning that a formula is proved.

---
## Slide 11: Hilbert system H

---
## Slide 12: Hilbert system H

---
## Slide 13: Hilbert system H

---
## Slide 14: The deduction rule
- To formalize the powerful methods of inference used in mathematics, we introduce derived inference rules.
- The most important derived rule is the deduction rule. Suppose that you want to prove A→B. Assume that A has already been proven and use it to prove B. This is not a proof of B unless A is an axiom or theorem that has been previously proved, in which case it can be used directly in the proof. However, we claim that the proof can be mechanically transformed into a proof of A→B.

---
## Slide 15: The deduction rule
- Example: The deduction rule is used frequently in mathematics. Suppose that you want to prove that the sum of any two odd integer numbers is even, expressed formally as:
- odd(x) ∧ odd(y)→even(x +y),
- for every x and y. To prove this formula, let us assume the formula odd(x) ∧ odd(y) as if it were an additional axiom. We have available all the theorems we have already deduced about odd numbers, particularly the theorem that any odd number can be expressed as 2k + 1. Computing:
- x +y = 2k1 +1+ 2k2 +1 = 2(k1 +k2 +1),
- we obtain that x+y is a multiple of 2, that is, even(x + y). The theorem now follows from the deduction rule, which discharges the assumption.

---
## Slide 16: The deduction rule

---
## Slide 17: The deduction rule

---
## Slide 18: The deduction rule

---
## Slide 19: Theorems for other operators
- So far, we have worked with only negation and implication as operators.
- These two operators are adequate for defining all others, so we can use these definitions to prove theorems using other operators.
- Recall that A ∧ B is defined as
  - ￢(A→￢B), and A ∨ B is defined as ￢A→B.

---
## Slide 20: Theorems for other operators

---
## Slide 21: Theorems for other operators

---
## Slide 22: Theorems for other operators

---
## Slide 23: Exercises

---
## Slide 24: Tasks
- Study all modules
- Read the PDF file of Chapter 3 shared with you
- Read the lecture notes
- Watch the lecture video files
- Do the assignments

---
## Slide 25: Logic for Computer ScienceCOT 3541
- Thank you
- Kiavash Bahreini, Ph.D.
- Associate Teaching Professor
- Knight Foundation School of Computing and Information Sciences (KFSCIS)
- School of computing and information sciences (SCIS)
- Florida international university (FIU)
- Module 9
