# Module5 - Logic for Computer Science COT 3541-1-1.pptx

> Source: `inbox/Module5 - Logic for Computer Science COT 3541-1-1.pptx` · type: pptx · ~1355 words · extracted 2026-10-24 13:00

---
## Slide 1: Logic for Computer ScienceCOT 3541
- Kiavash Bahreini, Ph.D.
- Associate Teaching Professor
- Knight Foundation School of Computing and Information Sciences (KFSCIS)
- School of computing and information sciences (SCIS)
- Florida international university (FIU)
- Module 5

---
## Slide 2: Content
- Logical equivalences
  - General logical equivalences
  - Logical equivalences involving conditional statements
  - Logical equivalences involving biconditionals
- Normal forms
  - Conjunctive normal form (CNF)
  - Disjunctive normal form (DNF)
- Converting to normal forms
- Why normal forms?

---
## Slide 3: Logical equivalences
- Definition: In logic and mathematics, statements p and q are said to be logically equivalent if they have the same truth value in every model.
- Symbols: The logical equivalence of p and q is sometimes expressed as p≡q (triple bar/tribar), p::q (a notation for equality of ratios), Epq, or p⟺q, depending on the notation.
- p≡q						Epq
- p::q						p⟺q

---
## Slide 4: General logical equivalences

| Equivalence | Name | Equivalence | Name |
|---|---|---|---|
| p ∧ T ≡ p p ∨ F ≡ p | Identity laws | (p ∨ q) ∨ r ≡ p ∨ (q ∨ r) (p ∧ q) ∧ r ≡ p ∧ (q ∧ r) | Associative laws |
| p ∨ T ≡ T p ∧ F ≡ F | Domination laws | p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r) p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) | Distributive laws |
| p ∨ p ≡ p p ∧ p ≡ p | Idempotent or tautology laws | ¬(p ∧ q) ≡ ¬p ∨ ¬q ¬(p ∨ q) ≡ ¬p ∧ ¬q | De Morgan's laws |
| ¬(¬p) ≡ p | Double negation law | p ∨ (p ∧ q) ≡ p p ∧ (p ∨ q) ≡ p | Absorption laws |
| p ∨ q ≡ q ∨ p p ∧ q ≡ q ∧ p | Commutative laws | p ∨ ¬p ≡ T p ∧ ¬p ≡ F | Negation laws |

---
## Slide 5: Logical equivalences involving conditional statements

| Equivalence | Equivalence |
|---|---|
| p ⇒ q ≡ ¬p ∨ q | (p ⇒ q) ∧ (p ⇒ r) ≡ p ⇒ (q ∧ r) |
| p ⇒ q ≡ ¬q ⇒ ¬p | (p ⇒ q) ∨ (p ⇒ r) ≡ p ⇒ (q ∨ r) |
| p ∨ q ≡ ¬p ⇒ q | (p ⇒ r) ∧ (q ⇒ r) ≡ (p ∨ q) ⇒ r |
| p ∧ q ≡ ¬(p ⇒ ¬q) | (p ⇒ r) ∨ (q ⇒ r) ≡ (p ∧ q) ⇒ r |
| ¬(p ⇒ q) ≡ p ∧ ¬q |  |

---
## Slide 6: Logical equivalences involving biconditionals

| Equivalence |
|---|
| p ⇔ q ≡ (p ⇒ q) ∧ (q ⇒ p) |
| p ⇔ q ≡ ¬p ⇔ ¬q |
| p ⇔ q ≡ (p ∧ q) ∨ (¬p ∧ ¬q) |
| ¬(p ⇔ q) ≡ p ⇔ ¬q |

---
## Slide 7: Assignment
- Using the truth tables, proof that all the formulas of general logical equivalences, logical equivalences involving conditional statements, and logical equivalences involving biconditionals are correct.

---
## Slide 8: Conjunctive normal form
- In propositional logic, a conjunctive normal form (CNF) is a clausal normal form of a logical formula consisting of a conjunction of disjunctions; it can also be described as an AND of ORs or a product of sums.
- Examples:
- (p)
- (p ∨ q)
- (p ∨ q) ∧ (r)
- (p ∨ ¬q ∨ ¬r) ∧ (¬a ∨ b ∨ c)
- For clarity, the disjunctive clauses are written inside parentheses.

---
## Slide 9: Conjunctive normal form
- The following formulas are not in conjunctive normal form:
- Non-examples:
- ¬(p ∨ q) Because an OR is nested within a NOT
- (p ∧ q) ∨ (r)
- p ∧ (q ∨ (s ∧ t)) Because an AND is nested within an OR

---
## Slide 10: Conjunctive normal form
- Every formula can be equivalently written as a formula in conjunctive normal form.
- Non-examples:
- ¬(p ∨ q) Because an OR is nested within a NOT
- (p ∧ q) ∨ (r)
- p ∧ (q ∨ (s ∧ t)) Because an AND is nested within an OR
- Non-examples can be converted to CNF:
- (¬p) ∧ (¬q)
- (p ∨ r) ∧ (q ∨ r)
- (p) ∧ (q ∨ s) ∧ (q ∨ t)

---
## Slide 11: Disjunctive normal form
- In propositional logic, a disjunctive normal form (DNF) is a canonical normal form of a logical formula consisting of a disjunction of conjunctions; it can also be described as an OR of ANDs or a sum of products.
- Examples:
- (p)
- (p ∧ q)
- (p ∧ q) ∨ (r)
- (p ∧ ¬q ∧ ¬r) ∨ (¬a ∧ b ∧ c)
- For clarity, the conjunctive clauses are written inside parentheses.

---
## Slide 12: Disjunctive normal form
- The following formulas are not in disjunctive normal form:
- Non-examples:
- ¬(p ∧ q) Because an AND is nested within a NOT
- ¬(p ∨ q) Because an OR is nested within a NOT
- p ∨ (q ∧ (s ∨ t)) Because an OR is nested within an AND

---
## Slide 13: Disjunctive normal form
- Every formula can be equivalently written as a formula in disjunctive normal form.
- Non-examples:
- ¬(p ∧ q) Because an AND is nested within a NOT
- p ∨ (q ∧ (s ∨ t)) Because an OR is nested within an AND
- Non-examples can be converted to DNF:
- (¬p) ∨ (¬q)
- (p) ∨ (q ∧ s) ∨ (q ∧ t))

---
## Slide 14: Converting to either normal forms
- We can turn any proposition into either normal form.
- We can use the definitions to get rid of →, ↔, and ⊕.
- Use DeMorgan's laws to move any ¬ in past parentheses so they sit on the variables.
- Use double negation to get rid of any ¬¬ that showed up.
- Use the distributive rules to move things in/out of parentheses as needed.
- For example, we can convert ¬((¬p→¬q)∧¬r) to conjunctive normal form:
- ¬((¬p→¬q)∧¬r)≡¬((¬¬p∨¬q)∧¬r) 	[Definition]
- ≡¬((p∨¬q)∧¬r) 			[Double negation]
- ≡¬(p∨¬q)∨¬¬r 			[DeMorgan’s]
- ≡¬(p∨¬q)∨r 			[Double negation]
- ≡(¬p∧¬¬q)∨r 			[DeMorgan’s]
- ≡(¬p∧q)∨r 			[Double negation]
- ≡(¬p∨r)∧(q∨r) 			[Distributive]
- It was actually in disjunctive normal form in the second-last step (≡(¬p∧q)∨r [double negation]).
- Normal Forms (sfu.ca)

---
## Slide 15: Converting to either normal forms
- For example, we can convert (p→q)→(¬r∧q) to disjunctive normal form:
- (p→q)→(¬r∧q)≡¬(p→q)∨(¬r∧q) 	[Definition]
- ≡¬(¬p∨q)∨(¬r∧q)			[Definition]
- ≡(¬¬p∧¬q)∨(¬r∧q) 		[DeMorgan’s]
- ≡(p∧¬q)∨(¬r∧q)			[Double negation]
- If we continue, we can convert it to conjunctive normal form, too.
- Normal Forms (sfu.ca)

---
## Slide 16: Converting to either normal forms
- So, let’s continue to convert (p→q)→(¬r∧q) to conjunctive normal form, too.
- (p→q)→(¬r∧q)≡¬(p→q)∨(¬r∧q) 	[Definition]
- ≡¬(¬p∨q)∨(¬r∧q)			[Definition]
- ≡(¬¬p∧¬q)∨(¬r∧q) 		[DeMorgan’s]
- ≡(p∧¬q)∨(¬r∧q)			[Double negation]
- ≡(p∨(¬r∧q))∧(¬q∨(¬r∧q))		[Distributive]
- ≡(p∨(¬r∧q))∧(¬q∨¬r)∧(¬q∨q)	[Distributive]
- ≡(p∨(¬r∧q))∧(¬q∨¬r)∧T		[Negation]
- ≡(p∨(¬r∧q))∧(¬q∨¬r)		[Identity]
- ≡(p∨¬r)∧(p∨q)∧(¬q∨¬r)		[Distributive]
- Normal Forms (sfu.ca)

---
## Slide 17: Why would we want to convert to a normal form?
- It may be easier to prove equivalence: to show A≡B, convert both to normal form and re-write one proof backward.
- Maybe we simplify a lot: if we end up with (p∨¬p∨⋯) terms, we know they are true.
- Proving theorems about all propositions: only have to handle Boolean expressions in a normal form, and that covers every proposition.
- Shows that we can use circuitry to calculate any Boolean expression with two layers of logic gates.
- Normal Forms (sfu.ca)

---
## Slide 18: Tasks
- Study all modules
- Read the PDF chapters shared with you
- Read the lecture notes
- Watch the lecture video files
- Do the assignments
