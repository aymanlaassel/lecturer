# Module7 - Semantic Tableaux - Logic for Computer Science COT 3541-1-1.pptx

> Source: `inbox/Module7 - Semantic Tableaux - Logic for Computer Science COT 3541-1-1.pptx` · type: pptx · ~1683 words · extracted 2026-10-24 13:00

---
## Slide 1: Logic for Computer ScienceCOT 3541
- Kiavash Bahreini, Ph.D.
- Associate Teaching Professor
- Knight Foundation School of Computing and Information Sciences (KFSCIS)
- School of computing and information sciences (SCIS)
- Florida international university (FIU)
- Module 7

---
## Slide 2: Content
- Decomposing formulas into sets of literals
- Semantic Tableaux
- Construction of semantic tableaux
- Termination of semantic tableaux
- Exercises

---
## Slide 3: Semantic tableaux
- Introduction
- It is an efficient decision procedure method for satisfiability in propositional logic.
- It is used to prove important theorems about deductive systems.
- The principle behind semantic tableaux
- Search for a model (satisfying interpretation) by decomposing the formula into sets of atoms and negations of atoms.
- A set of atoms and negations of atoms is satisfiable iff the set does not contain an atom p and its negation ¬p.
- The formula is satisfiable iff one of these sets is satisfiable.

---
## Slide 4: Decomposing formulas into sets of literals
- Definition
- A literal is an atom or the negation of an atom.
- An atom is a positive literal, and the negation is a negative literal.
- For any atom p
  - Set {p, ¬p} is a complementary pair of literals.
- For any formula A
  - Set {A, ¬A} is a complementary pair of formulas.

---
## Slide 5: Decomposing formulas into sets of literals
- Example
- q and r are positive literals and ¬p and ¬r are negative literals in the set of literals {¬p, q, r, ¬r}. This set contains the complementary pair of literals {r, ¬r}.

---
## Slide 6: Decomposing formulas into sets of literals
- Example
- Analyze the satisfiability of the formula:
  - A = p ^ (¬q ∨ ¬p)
    - In an arbitrary interpretation I using the indictive rules for the evaluation of the truth value of a formula.
  - Step 1: The principal operator of A is a conjunction, so vI (A) = T if and only if both vI (p) = T and vI (¬q ∨¬p) = T.
  - Step 2: The principal operator of ¬q ∨ ¬p is disjunction, so vI (¬q ∨¬p) = T if and only if either vI (¬q) = T or vI (¬p) = T.
  - Step 3: Integrating the information we have obtained from this analysis, we conclude that
    - vI (A) = T if and only if either:
      - 1. vI (p) = T and vI (¬q) = T , or
      - 2. vI (p) = T and vI (¬p) = T.
- Result: A is satisfiable if and only if there is an interpretation such that (1) holds or an interpretation such that (2) holds.
- Conclusion: We have reduced the question of the satisfiability of A to a question about the satisfiability of sets of literals.

---
## Slide 7: Decomposing formulas into sets of literals
- Theorem 1: A set of literals is satisfiable if and only if it does not contain a complementary pair of literals.
- Proof: Let L be a set of literals that does not contain a complementary pair. Define the interpretation I by:
  - I(p) = T if p ∈ L,
  - I(p) = F if ¬p ∈ L.
- The interpretation is well-defined—there is only one value assigned to each atom in L--since there is no complementary pair of literals in L. Each literal in L evaluates to T, so L is satisfiable.
- Conversely, if {p, ¬p} ⊆ L, then for any interpretation I for the atoms in L, either vI (p) = F or vI (¬p) = F, so L is not satisfiable.

---
## Slide 8: Decomposing formulas into sets of literals
- Example:
  - Continuing the analysis of the formula A = p∧(¬q∨¬p) from the previous example, A is satisfiable if and only at least one of the sets {p, ¬p} and {p, ¬q} does not contain a complementary pair of literals.
  - Clearly, only the second set does not contain a complementary pair of literals. Using the method described in Theorem 1, we obtain the  interpretation:
      - I(p) = T, 	I(q) = F.
      - Can you check that vI (A) = T for this interpretation?

---
## Slide 9: Decomposing formulas into sets of literals
- The following example shows what happens if a formula is unsatisfiable.
- Example:
- Consider the formula: B = (p ∨ q) ∧ (¬p ∧ ¬q).
- The analysis of the formula proceeds as follows:
- vI (B) = T if and only if vI (p ∨ q) = T and vI (¬p∧¬q) = T .
- Decomposing the conjunction, vI (B)=T if and only if vI (p ∨ q) = T and vI (¬p) = vI (¬q) = T.
- Decomposing the disjunction, vI (B) = T if and only if either:
  - 1. vI (p) = vI (¬p) = vI (¬q) = T , or
  - 2. vI (q) = vI (¬p) = vI (¬q) = T.
- Both sets of literals {p, ¬p, ¬q} and {q, ¬p, ¬q} contain complementary pairs, so by Theorem 1, both sets of literals are unsatisfiable. We conclude that it is impossible to find a model for B; in other words, B is unsatisfiable.

---
## Slide 10: Semantic tableaux
- Circled dot operator
- X operator
- Figure 1.

> **Speaker notes:** In the method of semantic tableaux, sets of formulas label nodes of a tree, where each path in the tree represents the formulas that must be satisfied in one possible interpretation. The initial formula labels the tree’s root; each node has one or two child nodes depending on how a formula labeling the node is decomposed. The sets of literals label the leaves. A leaf labeled by a set of literals containing a complementary pair of literals is marked ×, while a leaf labeled by a set not containing a complementary pair is marked ⊙.

---
## Slide 11: Construction of semantic tableaux
- The decomposition of a formula into sets of literals is rather difficult to follow when expressed textually, as we did in the previous examples.
- In the method of semantic tableaux, sets of formulas label nodes of a tree, where each path in the tree represents the formulas that must be satisfied in one possible interpretation.
- In semantic tableaux:
  - The initial formula labels the root of the tree
  - Each node has one or two child nodes depending on how a formula labeling the node is decomposed
  - The leaves are labeled by the sets of literals
  - A leaf labeled by a set of literals containing a complementary pair of literals is marked ×
  - While a leaf labeled by a set not containing a complementary pair is marked ⊙

> **Speaker notes:** In the method of semantic tableaux, sets of formulas label nodes of a tree, where each path in the tree represents the formulas that must be satisfied in one possible interpretation. The initial formula labels the tree’s root; each node has one or two child nodes depending on how a formula labeling the node is decomposed. The sets of literals label the leaves. A leaf labeled by a set of literals containing a complementary pair of literals is marked ×, while a leaf labeled by a set not containing a complementary pair is marked ⊙.

---
## Slide 12: Construction of semantic tableaux
- Figure 1 shows semantic tableaux for the formulas from the examples A and B. The tableau construction is not unique; here is another tableau for B:

---
## Slide 13: Construction of semantic tableaux
- Let’s compare both semantic tableaux for example B
- B

---
## Slide 14: Construction of semantic tableaux
- Classification of α- and β-formulas

---
## Slide 15: Construction of semantic tableaux
- Algorithm 1
  - Construction of a semantic tableau
  - Input: A formula φ of propositional logic.
  - Output: A semantic tableau T for φ all of whose leaves are marked.
  - Initially, T is a tree with a single root node labeled with the singleton set {φ}. This node is not marked.
  - Repeat the following step as long as possible: Choose an unmarked leaf l labeled with a set of formulas U(l) and apply one of the following rules.
  - U(l) is a set of literals. Mark the leaf closed × if it contains a complementary pair of literals. If not, mark the leaf open ⊙
  - U(l) is not a set of literals. Choose a formula in U(l) that is not a literal.
    - Classify the formula as an α-formula A or as a β-formula B and perform one of the following steps according to the classification:

---
## Slide 16: Termination of the Tableau Construction
- Definition 1: A tableau whose construction has terminated is a completed tableau.
- A completed tableau is closed if all its leaves are marked closed.
- Otherwise (if some leaf is marked open), it is open.

---
## Slide 17: Termination of the Tableau Construction
- Theorem 2: Constructing a tableau for any formula φ terminates.
  - When the construction terminates, all the leaves are marked × or ⊙

---
## Slide 18: Exercises
- Prove the following logical equivalences using semantic tableaux:
- A→B ≡ A↔(A ∧ B),
- A→B ≡ B ↔(A ∨ B),
- A ∧ B ≡ (A↔B)↔(A ∨ B),
- A↔B ≡ (A ∨ B)→(A ∧ B).

---
## Slide 19: Exercises
- Solution: 1. A→B ≡ A↔(A ∧ B): Refer to Canvas.

---
## Slide 20: Tasks
- Study all modules
- Read the PDF chapters shared with you
- Read the lecture notes
- Watch the lecture video files
- Do the assignments

---
## Slide 21: Logic for Computer ScienceCOT 3541
- Thank you
- Kiavash Bahreini, Ph.D.
- Associate Teaching Professor
- Knight Foundation School of Computing and Information Sciences (KFSCIS)
- School of computing and information sciences (SCIS)
- Florida international university (FIU)
- Module 7
