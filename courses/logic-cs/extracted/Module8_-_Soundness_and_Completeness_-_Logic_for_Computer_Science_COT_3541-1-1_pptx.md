# Module8 - Soundness and Completeness - Logic for Computer Science COT 3541-1-1.pptx

> Source: `inbox/Module8 - Soundness and Completeness - Logic for Computer Science COT 3541-1-1.pptx` · type: pptx · ~642 words · extracted 2026-10-24 13:00

---
## Slide 1: Logic for Computer ScienceCOT 3541
- Kiavash Bahreini, Ph.D.
- Associate Teaching Professor
- Knight Foundation School of Computing and Information Sciences (KFSCIS)
- School of computing and information sciences (SCIS)
- Florida international university (FIU)
- Module 8

---
## Slide 2: Content
- Soundness
- Completeness
- An example

---
## Slide 3: Soundness
- All theorems that can be proved in the logical system are true.
- A proof system is sound if everything that is provable is true. In other words, if φ1, …, φn⊢ψ then φ1, …, φn⊨ψ.
- If we prove something, then it is true.
- If something is provable, it is valid. If ⊢φ, then ⊨φ.
- We show the "truth" using (⊨) (double turnstile)
- and the "provability" using (⊢) (turnstile)

---
## Slide 4: Completeness
- All true statements can be proved in the logical system.
- A proof system is complete if everything that is true has a proof. In other words, if φ1, …, φn⊨ψ then φ1, …, φn⊢ψ.
- If something is true, then we can prove it.
- If something is valid, it is provable. If ⊨φ, then ⊢φ.
- We show the "truth" using (⊨) (double turnstile)
- and the "provability" using (⊢) (turnstile)

---
## Slide 5: Soundness
- Theorem 1: Soundness and completeness: Let T be a completed tableau for a formula A.
  - A is unsatisfiable if and only if T is closed.
- Here are some corollaries that follow from the theorem.
  - Corollary 1: A is satisfiable if and only if T is open.
  - Corollary 2: A is valid if and only if the tableau for ￢A closes.
  - Corollary 3: The method of semantic tableaux is a decision procedure for validity in propositional logic.

---
## Slide 6: Proof of soundness and completeness
- For soundness: if the tableau T for a formula A closes, then A is unsatisfiable.
- For completeness: if A is unsatisfiable, then every tableau for A closes.

---
## Slide 7: An example
- Security Analysis Tool
- Consider a security analysis tool T that tells if the given program P leaks user information (vulnerability X). So, given a program P, T says either P has vulnerability X or P does not have vulnerability X. We will use T’s verdict to advise folks to use or not use P.
  - If T was sound and said P has vulnerability X, then users should not use P because T can be trusted with this verdict — P is vulnerable with X.
  - If T was sound and said P does not have vulnerability X, then users should further examine P before choosing to use it because T cannot be trusted with this verdict — P may be vulnerable with X.
  - If T was complete and said P has vulnerability X, then users should further examine P before choosing to use it because T cannot be trusted with this verdict — P may not be vulnerable with X.
  - If T was complete and said P does not have vulnerability X, then users should use P because T can be trusted with this verdict — P is not vulnerable with X.
- Soundness and Completeness. Given a technique/system T that… | by Venkatesh-Prasad Ranganath | Medium

---
## Slide 8: Tasks
- Study all modules
- Read pages 39 to 45 of the PDF chapter 2 shared with you
- Read the lecture notes
- Watch the lecture video files
- Do the assignments

---
## Slide 9: Logic for Computer ScienceCOT 3541
- Thank you
- Kiavash Bahreini, Ph.D.
- Associate Teaching Professor
- Knight Foundation School of Computing and Information Sciences (KFSCIS)
- School of computing and information sciences (SCIS)
- Florida international university (FIU)
- Module 8
