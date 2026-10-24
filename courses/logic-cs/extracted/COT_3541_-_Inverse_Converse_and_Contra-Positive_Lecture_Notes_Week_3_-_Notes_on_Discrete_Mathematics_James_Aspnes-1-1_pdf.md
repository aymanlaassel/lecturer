# COT 3541 - Inverse, Converse, and Contra-Positive Lecture Notes Week 3 - Notes on Discrete Mathematics James Aspnes-1-1.pdf

> Source: `inbox/COT 3541 - Inverse, Converse, and Contra-Positive Lecture Notes Week 3 - Notes on Discrete Mathematics James Aspnes-1-1.pdf` · type: pdf · ~1961 words · extracted 2026-10-24 13:00

---
## Page 1

CHAPTER 2. MATHEMATICAL LOGIC 
21 
2.2.3.1 
Inverses, converses, and contrapositives 
The contrapositive of p > q is q > □p; it is logically equivalent to the 
original implication. For example, the contrapositive of "If I am human 
then I am a mammal" is "If I am not a mammal then I am not human". A 
proof by contraposition demonstrates that p implies q by assuming q 
and then proving p; it is similar but not identical to an indirect proof, 
which assumes p and derives a contradiction. 
The inverse of p > q is p > □q. So the inverse of "If you take CPSC 
202, you will surely die" is "If you do not take CPSC 202, you will not surely 
die." There is often no connection between the truth of an implication and 
the truth of its inverse: "If I am human then I am a mammal" does not 
have the same truth-value as "If I am not human then I am not a mammal," 
barring some over-the-top ecological disaster. 
The converse of p> q is q -+ p. E.g. the converse of "If I am human 
then I am a mammal" is "If I am a mammal then I am human." The converse 
of a statement is always logically equivalent to the inverse. Often in proving a 
biconditional (e.g. , "I am human and only if I am a mammal") , one proceeds 
by proving first the implication in one direction and then either the inverse 
or the converse, as either is logically equivalent to the implication in the 
other direction. 
2.2.3.2 
Equivalences involving true and false 
Any tautology is equivalent to true; any contradiction is equivalent to false. 
Two important cases of this are the law of the excluded middle 
PV-P=1 
and its dual, the law of non-contradiction 
P A-P =0. 
The law of the excluded middle is what allows us to do case analysis, where 
we prove that some proposition Q holds by showing first that P implies Q 
and then that P also implies Q. 4 
*Though we will use the law of the excluded middle, it has always been a little bit 
controversial, because it is non-constructive: it tells you that one of P or P is true, 
but it doesn't tell you which. 
For this reason, some logicians adopt a variant of classical logic called intuitionistic 
logic where the law of the excluded middle does not hold. Though this was originally 
done for aesthetic reasons, it turns out that there is a deep connection between computer

---
## Page 2

CHAPTER 2. MATHEMATICAL LOGIC 
22 
One strategy for simplifying logical expressions is to try to apply known 
equivalences to generate sub-expressions that reduce to true or false via the 
law of the excluded middle or the law of non-contradiction. These can then 
be absorbed into nearby terms using various absorption laws, shown in 
Table 2.3 . 
Example 
Let's show that (P A (P > Q)) > Q is a tautology. 
(This 
justifies the inference rule modus ponens, defined below.) Working from the 
programs and proofs in intuitionistic logic, known as the Curry-Howard isomorphism. 
The idea is that you get intuitionistic logic if you interpret 
• P as an object of type P; 
• P ---+ Q as a function that takes a P as an argument and returns a Q; 
• P A Q as an object that contains both a P and a Q (like a struct in C); 
• P V Q as an object that contains either a P or a Q (like a union in C); and 
• -P as P◊ , a function that given a P produces a special error value L that can't 
otherwise be generated. 
With this interpretation, many theorems of classical logic continue to hold. For example, 
modus ponens says 
(P A (P > Q)) > Q. 
Seen through the Curry-Howard isomorphism, this means that there is a function that, 
given a P and a function that generates a Q from a P, generates a Q. For example, the 
following Scheme function: 
(define (modus-ponens p p-implies q) (p-implies-q p)) 
Similarly, in a sufficiently sophisticated programming language we can show P ◊ --P, 
since this expands to P ◊ ((P ◊ L) Ö L), and we can write a function that takes a P as 
its argument and returns a function that takes a P ---+ ..l function and feeds the P to it: 
(define (double-negation p) (lambda (p-implies-fail) 
(p-implies-fail p))) 
But we can't generally show -,-,p ---+ P, since there is no way to take a function of type 
(P ---+ ..l) ---+ ..l and extract an actual example of a P from it. Nor can we expect to show 
P V -P, since this would require exhibiting either a P or a function that takes a P and 
produces an error, and for any particular type P we may not be able to do either. 
For normal mathematical proofs, we won't bother with this, and will just assume PVP 
always holds.

---
## Page 3

CHAPTER 2. MATHEMATICAL LOGIC 
23 
P AO = 0 
Pv0=P 
PA 1=P 
Pv1=1 
Po0=-P 
PO0=P 
Po1=P 
PO1=-P 
P>0=-P 
0 > P =1 
P>1=l 
1>P=P 
Table 2.3: Absorption laws. The first four are the most important. Note 
that A, V, ©, and u are all commutative, so reversed variants also work. 
inside out, we can compute 
(P A (P > Q)) > Q = (P A (-P V Q)) > Q 
= ((P A -P) V (P A Q)) > Q 
v (0 V (P A Q)) > Q 
= (P A Q) > Q 
v -(P A Q) V Q 
v (-P V -Q) V Q 
= -P V (-Q v Q) 
v -P V1 
v 1 
expand w 
distribute V over /\ 
non-contradiction 
absorption 
expand w 
De Morgan's law 
associativity 
excluded middle 
absorption 
In this derivation, we've labeled each step with the equivalence we used. 
Most of the time we would not be this verbose. 
2.2.4 
Normal forms 
A compound proposition is in conjunctive normal forrn ( CNF for short) 
if it is obtained by ANDing together ORs of one or more variables or their 
negations (an OR of one variable is just the variable itself). So for example 
P, (P V Q) A R, (P V Q) A (Q V R) A (P), and (P V Q) A (P V -R) A 
(-P V Q V S V T V -U) are in CNF, but (P V Q) A (P V -R) A (-P A Q), 
(PVQ)A (P ◊ R)A (-P V Q), and (P V (Q A R)) A (P V -R) A (-P V Q) are 
not. Using the equivalence P > Q = -P V Q, De Morgan's laws, and the 
distributive law, it is possible to rewrite any compound proposition in CNF.

---
## Page 4

CHAPTER 2. MATHEMATICAL LOGIC 
24 
This doesn't necessarily produce the simplest CNF . A famous Zen koan 
involves a student going for instruction to a swordmaster who also happens 
to be a Zen monk. The master tells the student "If you draw your sword, 
I will cut off your head. If you do not draw your sword, I will cut off your 
head." How should the student interpret this alarming statement? 
Writing P for the proposition that the student draws his sword and Q 
for the proposition that the master cuts off his head, we can immediately 
convert this to CNF by expanding the implications: 
(P > Q) A (-P > Q) = (-P V Q) A (P V Q) 
If we then attempt to simplify this by applying, say, the distributive law, 
it makes things worse: 
(-PVQ)A(P VQ) = (-P AP) V (-P A Q ) V (Q A P) V (Q A Q ) 
= 0 V (-P A Q) V (Q A P) V Q 
=(-PAQ)V (Q A P) V Q. 
Now the proposition is in disjunctive normal form, which means it's 
an OR of ANDs. If we look closely at the clauses, we realize that the Q clause 
by itself controls the outcome of the OR, since if either of the other clauses 
are true, so is Q.5 So in fact a simpler CNF version of this proposition is 
just Q alone, which is a not very big AND over a single not very big OR 
clause. Having simplified to Q, we realize that what the master just said was 
"I will cut off your head." It's time for the student to draw his sword! 
CNF formulas are particularly useful because they support resolution 
(see §2.4.1) . 
Using the tautology (P V Q) A (-P V R) > Q V R, we can 
construct proofs from CNF formulas by looking for occurrences of some 
simple proposition and its negation and resolving them, which generates a 
new clause we can add to the list. For example, we can compute 
(P V Q ) A (P V -R) A (-P V Q ) A (-Q V R) 
-(P VQ) A (P V -R) A (P V Q) A ( -Q V R) A Q 
(P VQ) A (P V -R) A (-P V Q) A (-Q V R) A Q A R 
-(P VQ)A (P V -R) A (-P V Q) A (-Q V R) A Q A R A P 
P. 
This style of proof is called a resolution proof. Because of its simplicity 
it is particularly well-suited for mechanical theorem provers. Such proofs 
5This is kind of a handwavy argument. If we want to justify this claim formally, we 
could write out a truth table.

---
## Page 5

CHAPTER 2. MATHEMATICAL LOGIC 
25 
can also encode traditional proofs based on modus ponens: the inference 
P A (P » Q) l Q can be rewritten as resolution by expanding > to get 
PA(-P V Q) - Q. 
Similarly, a compound proposition is in disjunctive normal form 
(DNF) if it consists of an OR of ANDs, e.g. (P A Q) V (P A -R) V (-P A Q). 
Just as any compound proposition can be transformed into CNF, it can 
similarly be transformed into DNF. DNF is sometimes easier to compute from 
truth tables, since we can include a AND clause recognizing each assignment 
that produces a 1, and OR them together.6 But this may not give us a very 
concise DNF. 
Note that conjunctive and disjunctive normal forms are not unique; for 
example, P A Q and (P V -Q) A (P V Q) A (P V Q) are both in conjunctive 
normal form and are logically equivalent to each other. So while CNF can be 
handy as a way of reducing the hairiness of a formula (by eliminating nested 
parentheses or negation of non-variables, for example), it doesn't necessarily 
let us see immediately if two formulas are really the same. 
2.3 
Predicate logic 
Using only propositional logic, we can express a simple version of a famous 
argument: 
• Socrates is a man. 
• If Socrates is a man, then Socrates is mortal. 
• Therefore, Socrates is mortal. 
This is an application of the inference rule called modus ponens, which 
says that from p and p ➔ q you can deduce q. The first two statements are 
axioms (meaning we are given them as true without proof), and the last is 
the conclusion of the argument. 
What if we encounter Socrates's infinitely more logical cousin Spocrates? 
We'd like to argue 
• Spocrates is a man. 
• If Spocrates is a man, then Spocrates is mortal. 
• Therefore, Spocrates is mortal. 
Using De Morgan's laws, the same works for CNF, where we include for each assignment 
that produces a O an OR clause that is false for that row.
