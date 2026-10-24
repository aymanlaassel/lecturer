# Module6 - Resolution - Logic for Computer Science COT 3541-1-1.pptx

> Source: `inbox/Module6 - Resolution - Logic for Computer Science COT 3541-1-1.pptx` · type: pptx · ~2057 words · extracted 2026-10-24 13:00

---
## Slide 1: Logic for Computer ScienceCOT 3541
- Kiavash Bahreini, Ph.D.
- Associate Teaching Professor
- Knight Foundation School of Computing and Information Sciences (KFSCIS)
- School of computing and information sciences (SCIS)
- Florida international university (FIU)
- Module 6

---
## Slide 2: Content
- Propositional resolution
  - Introduction
- Clausal Form
- Propositional resolution
  - Explanation
- Propositional resolution
  - Usages
- Propositional resolution
  - Resolution provability
- Exercises

---
## Slide 3: Reminder: logical equivalences
- Definition: In logic and mathematics, statements p and q are said to be logically equivalent if they have the same truth value in every model.
- Symbols: The logical equivalence of p and q is sometimes expressed as p≡q (triple bar/tribar), p::q (a notation for equality of ratios), Epq, or p⟺q, depending on the notation.
- p≡q						Epq
- p::q						p⟺q

---
## Slide 4: Propositional resolution
- Introduction
- It is an extremely powerful rule of inference for propositional logic.
- It is possible to build a theorem prover that is sound and complete for all of the propositional logic.
- The propositional resolution search space is much smaller than standard propositional logic.

---
## Slide 5: Clausal form
- Propositional resolution works only on expressions in clausal form.
- The premises and conclusions must be converted to this form before applying the rule.
- There is a simple procedure for making this conversion.

---
## Slide 6: Clausal form
- Literals
- A literal is either an atomic sentence or a negation of an atomic sentence.
- For example, if p is a logical constant, the following sentences are both literals:
  - P
  - ¬p
- A clause expression is either a literal or a disjunction of literals.
- If p and q are logical constants, then the following are clause expressions:
  - P
  - ¬p
  - p ∨ q

---
## Slide 7: Clausal form
- A clause expression is either a literal or a disjunction of literals.
- If p and q are logical constants, then the following are clause expressions:
  - P
  - ¬p
  - p ∨ q
- A clause is the set of literals in a clause expression. For example, the following sets are the clauses corresponding to the clause expressions above.
  - {p}
  - {¬p}
  - {p, q}
- Note: An empty set {} is also a clause. It is equivalent to an empty disjunction and, therefore, is unsatisfiable.

---
## Slide 8: Converting propositional logic to clausal form
- The following conversion rules should be applied in order:
  - 1. Implications (I)
  - 2. Negations (N)
  - 3. Distribution (D)
  - 4. Operators (O)

---
## Slide 9: Converting propositional logic to clausal form
- The following conversion rules should be applied in order:

| 1. Implications (I):  ϕ1 ⇒ϕ2 → ¬ϕ1 ∨ϕ2  ϕ2 ⇒ ϕ1 → ¬ϕ2 ∨ ϕ1  ϕ1 ⇔ ϕ2 → (¬ϕ1 ∨ϕ2 ) ∧ (ϕ1 ∨ ¬ϕ2 ) | 3. Distribution (D): ϕ1 ∨ (ϕ2 ∧ϕ3 ) → (ϕ1 ∨ϕ2 ) ∧(ϕ1 ∨ϕ3 )  (ϕ1 ∧ϕ2 ) ∨ϕ3 → (ϕ1 ∨ϕ3 ) ∧ (ϕ2 ∨ϕ3 )  (ϕ1 ∨ϕ2 ) ∨ϕ3 → ϕ1 ∨(ϕ2 ∨ϕ3 )  (ϕ1 ∧ϕ2 ) ∧ϕ3 → ϕ1 ∧(ϕ2 ∧ϕ3 ) |
|---|---|
| 2. Negations (N): ¬¬ϕ → ϕ ¬(ϕ1 ∧ϕ2) → ¬ϕ1 ∨ ¬ϕ2 ¬(ϕ1 ∨ϕ2) → ¬ϕ1 ∧ ¬ϕ2 | 4. Operators (O): ϕ1 ∨... ∨ϕn → {ϕ1 ,...,ϕn }  ϕ1 ∧ ...∧ϕn → {ϕ1 }...{ϕn } |

---
## Slide 10: Converting propositional logic to clausal form
- Example 1: Convert (g ∧ (r ⇒ f)) to clausal form
  - g ∧ (r ⇒ f )
  - I         g ∧ (¬r ∨ f)
  - N     g ∧ (¬r ∨ f)
  - D      g ∧ (¬r ∨ f)
  - O      {g}
  - {¬r, f}

---
## Slide 11: Converting propositional logic to clausal form
- Example 2: Convert ¬(g ∧ (r ⇒ f )) to clausal form
  - ¬(g ∧ (r ⇒ f ))
  - I         ¬(g ∧ (¬r ∨ f ))
  - N     ¬g ∨ ¬(¬r ∨ f))
  - ¬g ∨(¬¬r ∧ ¬f )
  - ¬g ∨(r ∧ ¬f )
  - D      (¬g ∨r) ∧(¬g ∨ ¬f)
  - O     {¬g,r}
  - {¬g,¬f}

---
## Slide 12: Converting propositional logic to clausal form
- Comparison of examples 1 and 2:
  - Even though the propositional logical expressions in examples 1 and 2 are similar to start with (disagreeing on just one ¬ operator), however, the results are quite different:

| Example 1 | Example 2 |
|---|---|
| {g} {¬r, f} | {¬g,r} {¬g,¬f} |

---
## Slide 13: Practice
- Convert the following propositional logical expressions to clausal form.
- 1. (p ⇒ q) ∧ (p ⇒ r)
- 2. ¬(p ⇔ q)
- 3. ¬(p ⇒ ¬q) ⇒ ¬(q ⇒ ¬r)

---
## Slide 14: Propositional resolution
- Explanation
- Suppose we know that p is true or q is true, and suppose we also know that p is false or r is true.
- One clause contains p, and the other contains ¬p. If p is false, then by the first clause, q must be true.
- If p is true, then, by the second clause, r must be true.
- Since p must be either true or false, then it must be the case that q is true or r is true. In other words, we can cancel the p literals.
  - {p,q}
  - {¬p,r}
  - ------
  - {q,r}

---
## Slide 15: Propositional resolution
- Generalization
- More generally, given a clause containing a literal c and another containing the literal Øc, we can infer that the clause consists of all the literals of both clauses without the complementary pair. This rule of inference is called propositional resolution.
- {j1,..., c,...,jm}
- {y1,...,Øc,...,yn}
- -------------------------
- {j1,...,jm,y1,...,yn}

---
## Slide 16: Propositional resolution
- More explanation
- Because clauses are sets, we do not have two literal occurrences in a clause. Therefore, in drawing a conclusion from two clauses that share a literal, we merge the two occurrences into one, as in the following example:
  - {Øp, q}
  - {p,q}
  - ---------
  - {q}

---
## Slide 17: Propositional resolution
- More explanation
- If either of the clauses is a singleton set, we see that the number of literals in the result is less than that in the other clause. From the clause {Øp,q} and the singleton clause {p}, we can derive the singleton clause {q}. Note the correspondence between this deduction and that of Modu  Ponens.
- {Øp, q}
- {p}
- ---------
- {q}

---
## Slide 18: Propositional resolution
- More explanation
- Resolving two singleton clauses leads to the empty clause, i.e., the clause consisting of no literals at all, as shown below. The derivation of the empty clause means that the database contains a contradiction.
- {p}
- {Øp}
- -------
- {}

---
## Slide 19: Propositional resolution
- More explanation
- If two clauses resolve, they may have more than one resolvent because there may be more than one way in which to choose the resolvents. Consider the following deductions.
- {p,q}
- {Øp,Øq}
- -----------
- {p,Øp}
- {q,Øq}

---
## Slide 20: Propositional resolution
- More explanation
- Note that only one pair of literals may be resolved at a time in resolving two clauses, even though there are multiple resolvable pairs. For example, the following is not a legal application of propositiona  resolution.
- {p,q}
- {Øp,Øq}	Wrong!
- -----------
- {}

---
## Slide 21: Propositional resolution
- More explanation
- Here are some common cases of resolution in action. The resolution derivations are shown on the right, and the corresponding natural deductions are shown on the left.

| Corresponding natural deductions | Resolution derivations |
|---|---|
| p ⇒ q P ------- Q | {¬p, q} {p} -------- {q} |
| p ⇒ q ¬q ------- ¬p | {¬p, q} {¬q} -------- {¬p} |
| p ⇒ q q ⇒ r ------- p ⇒ r | {¬p, q} {¬q, r} -------- {¬p, r} |

---
## Slide 22: Propositional resolution
- Usages
- To determine whether a set of clauses is unsatisfiable, we look for a resolution proof of the empty clause from the set of premises.
- 1. {p,q} 		Premise
- 2. {¬p, q} 	Premise
- 3. {p, ¬q} 	Premise
- 4. {¬p, ¬q} 	Premise
- 5. {q} 		1,2
- 6. {¬q} 		3,4
- 7. {} 		5,6

---
## Slide 23: Propositional resolution
- Validity checking
- Validity checking is a little more difficult. The problem is that propositional resolution is not generatively complete, i.e. we cannot directly derive all consequences from a set of premises. For example, we cannot directly derive (p ⇒ (q ⇒ p)) using propositional resolution. There are no premises. Consequently, there are no conclusions. This apparent problem disappears if we take the clausal form of the premises (if any) together with the negated goal and try to derive the empty clause. The conversion to clausal form is shown below. From here, it is easy to see the result; the {p} and {Øp} clauses resolve to produce the empty clause in a single step.
- Ø( pÞ (q Þ p))
- I 	Ø(Øp Ú Øq Ú p)
- N 	ØØp Ù ØØq ÙØp
- p Ù q Ù Øp
- D 	p Ù q Ù Øp
- O 	{p}
- {q}
- {Øp}

---
## Slide 24: Propositional resolution
- Validity checking
- To determine whether a set D of sentences logically entails a sentence j, rewrite DÈ{Øj} in clausal form and try to derive the empty clause. Suppose, for example, we began with the premises (p Þ q) and (q Þ r) and we want to prove (p Þ r). To do this, we add the negation of the conclusion, i.e., Ø(p Þ r), and derive the empty clause.
- 1. {Øp, q} 	Premise
- 2. {Øq,r} 	Premise
- 3. {p} 		Negated Goal
- 4. {Ør} 		Negated Goal
- 5. {q} 		3,1
- 6. {r} 		5,2
- 7. {} 		6,4

---
## Slide 25: Propositional resolution
- Validity checking
- As another example, consider the case of Sabrina, Gabriel, and Lily. We know that, if Sabrina loves Gabriel, then Sabrina loves Lily. We also know that, if it is Wednesday, then Sabrina loves Gabriel or Lily. Our task is to prove that, if it is Wednesday, then Sabrina loves Lily. The proof goes as follows.
- 1. {Øp, q} Premise
- 2. {Øm, p,q} Premise
- 3. {m} Negated Goal
- 4. {Øq} Negated Goal
- 5. {p,q} 3,2
- 6. {q} 5,1
- 7. {} 6,4

---
## Slide 26: Propositional resolution
- Resolution provability
- A sentence j is provable from a set of sentences D by propositional resolution (written D |- j) if and only if there is a derivation of the empty clause from the clausal form of DÈ{Øj}.
- Resolution Theorem: Propositional Resolution is sound and complete, i.e., D |= j if and only if D |- j.
- One nice feature of propositional resolution vis-a-vis the more general proof method described in the preceding chapter is that propositional resolution always terminates. We simply search the resolution graph in a breadth-first fashion. Since only finitely many clauses can be constructed from a finite set of logical constants, the procedure will eventually run out of new conclusions to draw.

---
## Slide 27: Practice
- Use propositional resolution to prove the following sentence.
- 1. (p Úq) Ù( pÞ r) Þ(p Þ r)
- Propositional Resolution. Use propositional resolution to show that the following sets of clauses are unsatisfiable.
- (a) {p,q}, {Øp,r}, {Øp,Ør},{p, Øq}
- (b) {p,q, Ør,s}, {Øp,r,s}, {Øq, Ør}, {p, Øs}, {Øp, Ør}, {r}

---
## Slide 28: Tasks
- Study all modules
- Read the PDF chapters shared with you
- Read the lecture notes
- Watch the lecture video files
- Do the assignments

---
## Slide 29: References
- Chapter 5 Propositional Resolution, URL.

---
## Slide 30: Logic for Computer ScienceCOT 3541
- Thank you
- Kiavash Bahreini, Ph.D.
- Associate Teaching Professor
- Knight Foundation School of Computing and Information Sciences (KFSCIS)
- School of computing and information sciences (SCIS)
- Florida international university (FIU)
- Module 6
