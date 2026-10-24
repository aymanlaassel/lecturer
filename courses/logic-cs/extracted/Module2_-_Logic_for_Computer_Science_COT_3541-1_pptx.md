# Module2 - Logic for Computer Science COT 3541-1.pptx

> Source: `inbox/Module2 - Logic for Computer Science COT 3541-1.pptx` · type: pptx · ~916 words · extracted 2026-10-24 13:00

---
## Slide 1: Logic for Computer ScienceCOT 3541
- Kiavash Bahreini, Ph.D.
- Associate Teaching Professor
- Knight Foundation School of Computing and Information Sciences (KFSCIS)
- School of computing and information sciences (SCIS)
- Florida international university (FIU)
- Module 2

---
## Slide 2: Content
- Truth table
- Precedence of connectives
- Propositional logic equivalences
- Properties of operators

---
## Slide 3: Truth table
- The truth table represents the behavior of a formula under all potential interpretations of the primitive propositions comprised in the formula.
- merriam-webster.com

---
## Slide 4: Truth table for negation (¬) (Not)
- The negation connective
  - Unary
  - One argument
  - Definition: If p is an arbitrary proposition, then the negation of p is written as ¬p and will be true iff p is false.
- Truth table for negation (¬)

| p | ¬p |
|---|---|
| True | False |
| False | True |

---
## Slide 5: Truth table for conjunction (∧) (And)
- The conjunction connective
  - Binary
  - Two arguments
  - Definition: If p and q are arbitrary propositions, then the conjunction of p and q is written as p ∧ q and consequently will be true iff both p and q are true.
- Truth table for conjunction (∧)

| p | q | p ∧ q |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---
## Slide 6: Truth table for disjunction (∨) (Or)
- The disjunction connective
  - Binary
  - Two arguments
  - Definition:  If p and q are arbitrary propositions, then the disjunction of p and q is written as p ∨ q and will be true iff either p is true, or q is true, or both p and q are true.
- Truth table for disjunction (∨)

| p | q | p ∨ q |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---
## Slide 7: Truth table for implication (→) (⇒)(If… then…)
- The implication (conditional) connective
  - Binary
  - Two arguments
  - Definition:  If p and q are arbitrary propositions, then the implication (conditional) of p and q is written as p ⇒ q or (p → q) and will be true iff either p is false or q is true.
- Truth table for implication (→)

| p | q | p → q |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | True |
| False | False | True |

---
## Slide 8: Truth table for biconditional (⇔) (if and only if) (iff)
- The biconditional connective
  - Binary
  - Two arguments
  - Definition:  If p and q are arbitrary propositions, then the biconditional of p and q is written: p ⇔ q and will be true iff either:
    - P and q are both true
    - P and q are both false
- Truth table for biconditional (⇔)

| p | q | p ⇔ q |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | True |

---
## Slide 9: Precedence of connectives

| Precedence | Operators |
|---|---|
| First precedence | Parenthesis |
| Second precedence | Negation |
| Third precedence | Conjunction (And) |
| Fourth precedence | Disjunction (Or) |
| Fifth precedence | Implication |
| Sixth precedence | Biconditional |

---
## Slide 10: Propositional logic equivalences

| p | q | ¬p | ¬p ∨ q | p → q |
|---|---|---|---|---|
| True | True | False | True | True |
| True | False | False | False | False |
| False | True | True | True | True |
| False | False | True | True | True |

---
## Slide 11: Properties of operators
- Commutativity
  - P ∧ Q = Q ∧ P
  - P ∨ Q = Q ∨ P

---
## Slide 12: Properties of operators
- Associativity
  - (P ∧ Q) ∧ R = P ∧ (Q ∧ R)
  - (P ∨ Q) ∨ R = P ∨ (Q ∨ R)

---
## Slide 13: Properties of operators
- Identity element
  - P ∧ True = P
  - P ∨ True = True

---
## Slide 14: Properties of operators
- Distributive
  - P ∧ (Q ∨ R) = (P ∧ Q) ∨ (P ∧ R)
  - P ∨ (Q ∧ R) = (P ∨ Q) ∧ (P ∨ R)

---
## Slide 15: Properties of operators
- DE Morgan's Law
  - ¬ (P ∧ Q) = (¬P) ∨ (¬Q)
  - ¬ (P ∨ Q) = (¬P) ∧ (¬Q)

---
## Slide 16: Properties of operators
- Double-negation elimination
  - ¬(¬P) = P

---
## Slide 17: Content
- Propositional logic equivalences
- Properties of operators
- Logical reasoning
- Propositional logic
  - Definition
  - Examples
  - Atomic propositions
- Propositional logic connectives
- The truth table
- Precedence of connectives

---
## Slide 18: Content for the next lecture
- Inverse, converse, and contra-positive
- Duality principle
- Normal forms
- Limitations of propositional logic
