# COT 3541 - Truth Tables Lecture Notes Week 2 Notes on Discrete Mathematics James Aspnes-1.pdf

> Source: `inbox/COT 3541 - Truth Tables Lecture Notes Week 2 Notes on Discrete Mathematics James Aspnes-1.pdf` · type: pdf · ~4348 words · extracted 2026-10-24 13:00

---
## Page 1

CHAPTER 2. MATHEMATICAL LOGIC 
16 
((p v q) V r) and as (p V (q V r)), and similarly (p A q A r) is the same as 
((pA q) A r) and as (p A (q A r)). 
Note that this convention is not universal: many mathematicians give 
AND and OR equal precedence, so that the meaning of p A q V r is ambigu­
ous without parentheses. There are good arguments for either convention. 
Making AND have higher precedence than OR is analogous to giving multi­
plication higher precedence than addition, and makes sense visually when 
AND is written multiplicatively (as in pq V qr for (p A q) V ( q A r). Making 
them have the same precedence emphasizes the symmetry between the two 
operations, which we'll see more about later when we talk about De Morgan's 
laws in §2.2.3. But as with anything else in mathematics, either convention 
can be adopted, as long as you are clear about what you are doing and it 
doesn't cause annoyance to the particular community you are writing for. 
There does not seem to be a standard convention for the precedence of 
XOR, since logicians don't use it much. There are plausible arguments for 
putting XOR in between AND and OR, but it's probably safest just to use 
parentheses. 
Implication is not associative, although the convention is that it binds 
"to the right," so that a > b > c is read as a > (b > c). Except for 
type theorists and Haskell programmers, few people ever remember this, 
so it is usually safest to put in the parentheses. I personally have no idea 
what p a q > ` means, so any expression like this should be written with 
parentheses as either (p a q) a r or p a (q > r). 
2.2.2 Truth tables 
To define logical operations formally, we give a truth table. This gives, for 
any combination of truth values (true or false, which as computer scientists 
we often write as 1 or 0) of the inputs, the truth value of the output. In this 
usage, truth tables are to logic what addition and multiplication tables are 
to arithmetic. 
Here is a truth table for negation: 
p
p 
p 
0 
1 
0 0 
CHAPTER 2. MATHEMATICAL LOGIC 
16 
((p v q) V r) and as (p V (q V r)), and similarly (p A q A r) is the same as 
((p A q) A r) and as (p A (q A )). 
Note that this convention is not universal: many mathematicians give 
AND and OR equal precedence, so that the meaning of p A q V r is ambigu­
ous without parentheses. There are good arguments for either convention. 
Making AND have higher precedence than OR is analogous to giving multi­
plication higher precedence than addition, and makes sense visually when 
AND is written multiplicatively ( as in pq V qr for (p A q) V ( q A r). Making 
them have the same precedence emphasizes the symmetry between the two 
operations, which we'll see more about later when we talk about De Morgan's 
laws in §2.2.3. But as with anything else in mathematics, either convention 
can be adopted, as long as you are clear about what you are doing and it 
doesn't cause annoyance to the particular community you are writing for. 
There does not seem to be a standard convention for the precedence of 
XOR, since logicians don't use it much. There are plausible arguments for 
putting XOR in between AND and OR, but it's probably safest just to use 
parentheses. 
Implication is not associative, although the convention is that it binds 
"to the right," so that a > b > c is read as a > (b > c). Except for 
type theorists and Haskell programmers, few people ever remember this, 
so it is usually safest to put in the parentheses. I personally have no idea 
what p b q b r means, so any expression like this should be written with 
parentheses as either (p b q) b r or p b (q <> r). 
2.2.2 Truth tables 
To define logical operations formally, we give a truth table. This gives, for 
any combination of truth values (true or false, which as computer scientists 
we often write as 1 or 0) of the inputs, the truth value of the output. In this 
usage, truth tables are to logic what addition and multiplication tables are 
to arithmetic. 
Here is a truth table for negation: 
0 
1 
1 1

---
## Page 2

CHAPTER 2. MATHEMATICAL LOGIC 
And here is a truth table for the rest of the logical operators: 
p q p V q p©q p\q p>q p n q 
0 
0 
0 
1 
1 
0
1 
1 
0 
1 
0 
1
0
1 
1 
0 
0 
0 
1
1
1 
0 
1 
1 
1 
See also [Fer08, §1.1], [Ros12, §§1.1-1.2], or [Big02, §§3.1-3.3]. 
17 
We can think of each row of a truth table as a model for propositional 
logic, since the only things we can describe in propositional logic are whether 
particular propositions are true or not. Constructing a truth table corre­
sponds to generating all possible models. 
This can be useful if we want to figure out when a particular proposition 
is true. Proving a proposition using a truth table is a simple version of 
model checking: we enumerate all possible models of a given collection 
of simple propositions, and see if what we want to prove holds in all models. 
This works for propositional logic because the list of models is just the list 
of possible combinations of truth values for all the simple propositions P, 
Q, etc. We can check that each truth table we construct works by checking 
that the truth values each column (corresponding to some subexpression of 
the thing we are trying to prove) follow from the truth values in previous 
columns according to the rules established by the truth table defining the 
appropriate logical operation. 
For predicate logic, model checking becomes more complicated, because 
a typical system of axioms is likely to have infinitely many models, many of 
which are likely to be infinitely large. There we will need to rely much more 
on proofs constructed by applying inference rules. 
2.2.3 
Tautologies and logical equivalence 
A compound proposition that is true no matter what the truth-values of the 
propositions it contains is called a tautology. For example, p ➔ p, p V p, 
and ,(p I\ ,p) are all tautologies, as can be verified by constructing truth 
tables. If a compound proposition is always false, it's a contradiction. The 
negation of a tautology is a contradiction and vice versa. 
The most useful class of tautologies are logical equivalences. This is a 
tautology of the form X +-+ Y, where X and Y are compound propositions. 
In this case, X and Y are said to be logically equivalent and we can 
substitute one for the other in more complex propositions. We write X 
Y 
if X and Y are logically equivalent. 
CHAPTER 2. MATHEMATICAL LOGIC 
And here is a truth table for the rest of the logical operators: 
p 
q pvq p©q p\q p > q p<>q 
0
0
0 
0 
0 
1 
1 
0
1
1 
1 
0 
1 
0 
1 
1 
0 
0 
0 
1
1 
0 
1 
1 
1 
See also [Fer08, §1.1], [Ros12, §§1.1-1.2], or [Big02, §§3.1-3.3]. 
17 
We can think of each row of a truth table as a model for propositional 
logic, since the only things we can describe in propositional logic are whether 
particular propositions are true or not. Constructing a truth table corre­
sponds to generating all possible models. 
This can be useful if we want to figure out when a particular proposition 
is true. Proving a proposition using a truth table is a simple version of 
model checking: we enumerate all possible models of a given collection 
of simple propositions, and see if what we want to prove holds in all models. 
This works for propositional logic because the list of models is just the list 
of possible combinations of truth values for all the simple propositions P, 
Q, etc. We can check that each truth table we construct works by checking 
that the truth values each column (corresponding to some subexpression of 
the thing we are trying to prove) follow from the truth values in previous 
columns according to the rules established by the truth table defining the 
appropriate logical operation. 
For predicate logic, model checking becomes more complicated, because 
a typical system of axioms is likely to have infinitely many models, many of 
which are likely to be infinitely large. There we will need to rely much more 
on proofs constructed by applying inference rules. 
2.2.3 
Tautologies and logical equivalence 
A compound proposition that is true no matter what the truth-values of the 
propositions it contains is called a tautology. For example, p > p, p V p, 
and -(p A p) are all tautologies, as can be verified by constructing truth 
tables. If a compound proposition is always false, it's a contradiction. The 
negation of a tautology is a contradiction and vice versa. 
The most useful class of tautologies are logical equivalences. This is a 
tautology of the form X +--+ Y, where X and Y are compound propositions. 
In this case, X and Y are said to be logically equivalent and we can 
substitute one for the other in more complex propositions. We write X 
Y 
if X and Y are logically equivalent.

---
## Page 3

p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
□p A -q 
CHAPTER 2. MATHEMATICAL LOGIC 
18 
The nice thing about logical equivalence is that is does the same thing for 
Boolean formulas that equality does for algebraic formulas: if we know (for 
example), that p V p is equivalent to 1, and q V 1 is equivalent to 1, we can 
grind q VpVp = q V 1 = 1 without having to do anything particularly clever. 
(We will need cleverness later when we prove things where the consequent 
isn't logically equivalent to the premise.) 
To prove a logical equivalence, one either constructs a truth table to show 
that X +--+ Y is a tautology, or transforms X to Y using previously-known 
logical equivalences. 
Some examples: 
• p A -p = 0: Construct a truth table 
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p 
p 
p 
p 
p 
p 
p 
□p p\op 
p\op 
p\op 
p\op 
p\op 
p\op 
p\op 
p K p 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
p 
p 
p 
p 
p 
p 
p 
□p p\op 
p\op 
p\op 
p\op 
p\op 
p\op 
p\op 
p K p 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
and observe that the last two columns are always equal. 
• p V p = p: Use the truth table 
p pVp 
0 0 
1 
1 
• p> q = -p V q: Again construct a truth table 
p q p > q 
□p V q 
0 0 
1 
1 
0 
1 
1 
1 
1 
0 
0 
0 
1 
1 
1 
1 
• -(pVq) = -pA-q: (one of De Morgan's laws; the other is -(p A q) I 
□p V -q). 
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p 
p 
p 
p 
p 
p 
p 
□p p\op 
p\op 
p\op 
p\op 
p\op 
p\op 
p\op 
p K p 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
p 
p 
p 
p 
p 
p 
p 
□p p\op 
p\op 
p\op 
p\op 
p\op 
p\op 
p\op 
p K p 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
p pVp
0 0 
1 
1 
• p> q = -p V q:
p q p > q 
□p V q 
0 0 
1 
1 
0 
1 
1 
1 
1 
0 
0 
0 
1 
1 
1 
1 
• -(pVq) = -pA-q: (one of De Morgan's laws; the other is -(p A q) I 
□p V -q). 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
p q pV q -(pV q) 
□p -q 
□p J □q 
0 0 
0 
1 
1 
1 
1 
0 
1 
1 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
1 
0 
0 
0 
0 
□p A -q
CHAPTER 2. MATHEMATICAL LOGIC 
18 
The nice thing about logical equivalence is that is does the same thing for 
Boolean formulas that equality does for algebraic formulas: if we know (for 
example), that p V p is equivalent to 1, and q V 1 is equivalent to 1, we can 
grind q VpVp = q V 1 = 1 without having to do anything particularly clever. 
(We will need cleverness later when we prove things where the consequent 
isn't logically equivalent to the premise.) 
To prove a logical equivalence, one either constructs a truth table to show 
that X +-+ Y is a tautology, or transforms X to Y using previously-known 
logical equivalences. 
Some examples: 
• p A -p = 0: Construct a truth table 
and observe that the last two columns are always equal. 
• p V p = p: Use the truth table 
p pVp 
0 
0 
1 
1 
• p > q = p V q: Again construct a truth table 
p q p > q -p V q 
0 
0 
1 
1 
0 
1 
1 
1 
1 
0 
0 
0 
1 
1 
1 
1 
• -(pVq) = -p-q: (one of De Morgan's laws; the other is □(p A q) L 
□p V -q).

---
## Page 4

CHAPTER 2. MATHEMATICAL LOGIC 
19 
• p V ( q Ar) = (pVq) A (pVr) ( one of the distributive laws; the other is 
pA (qVr) = (pAq)V(pAr)). 
p q 
1 
q A r pV(qAr) pVq pVr (pvq) A (pVr) 
0 0 0 
0 
0 
0 
0 
0 
0 0 
1 
0 
0 
0 
1 
0 
0 
1 
0 
0 
0 
1 
0 
0 
0 
1 
1 
1 
1 
1 
1 
1 
1 
0 0 
0 
1 
1 
1 
1 
1 
0 
1 
0 
1 
1 
1 
1 
1 
1 
0 
0 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
• (p > r) V (q > r) 
(p A q) > r. Now things are getting messy, 
so building a full truth table may take a while. But we have take a 
shortcut by using logical equivalences that we've already proved (plus 
associativity of V): 
[Using 
[Using 
[Using 
[Using p> 
p> 
p> 
p > q = -pVq 
-pVq 
-pVq 
p V q twice] 
twice] 
twice] 
twice] 
[De 
[De 
[De 
[De Morgan's 
Morgan's 
Morgan's 
Morgan's law] 
law] 
law] 
law] 
= (pAq)gr. 
[p> q = -pvq] 
This last equivalence is a little surprising. It shows, for example, that 
if somebody says "It is either the case that if you study you will graduate 
from Yale with distinction, or that if you join the right secret society you 
will graduate from Yale with distinction", then this statement (assuming 
we treat the or as V) is logically equivalent to "If you study and join the 
right secret society, then you will graduate from Yale with distinction." It is 
easy to get tangled up in trying to parse the first of these two propositions; 
translating to logical notation and simplifying using logical equivalence is a 
good way to simplify it. 
Over the years, logicians have given names to many logical equivalences. 
Some of the more useful ones are summarized in Table 2.2. More complicated 
equivalences can often be derived from these. If that doesn't work (and you 
don't have too many variables to work with), you can always try writing out 
a truth table. 
• p V ( q Ar) = (pVq) A (pVr) ( one of the distributive laws; the other is 
pA (qVr) = (pAq)V(pAr)). 
[Using 
[Using 
[Using 
[Using p> 
p> 
p> 
p > q = -pVq 
-pVq 
-pVq 
p V q twice] 
twice] 
twice] 
twice] 
[De 
[De 
[De 
[De Morgan's 
Morgan's 
Morgan's 
Morgan's law] 
law] 
law] 
law] 
= (pAq)gr. 
[p> q = -pvq] 
CHAPTER 2. MATHEMATICAL LOGIC 
19 
• p V (q Ar) = (pV q) A (p V r) (one of the distributive laws; the other is 
pA(qVr) = (pAq) V(pAr)). 
p 
q 
r 
q /A r pV(qAr) 
pVq pVr (pVq) A (pVr) 
0 0 
0 
0 
0 
0 
0 
0 
0 0 
1 
0 
0 
0 
1 
0 
0 
1 
0 
0 
0 
1 
0 
0 
0 
1 
1 
1 
1 
1 
1 
1 
1 
0 
0 
0 
1 
1 
1 
1 
1 
0 
1 
0 
1 
1 
1 
1 
1 
1 
0 
0 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
• (p > r) V (q > r) 
(p A q) > r. Now things are getting messy, 
so building a full truth table may take a while. But we have take a 
shortcut by using logical equivalences that we've already proved (plus 
associativity of V): 
(phr
(pgr)v(q-r)
(pgr)v(q-r)
(pgr)v(q-r)
) V (q h r) = = (-pvr)v(-qVr) 
(-pvr)v(-qVr) 
(-pvr)v(-qVr) 
(p Vr) V (-qV r) 
i = -pV-qVrVr 
-pV-qVrVr 
-pV-qVrVr 
-pV-qVrVr 
i 
=-pv-qvr 
=-pv-qvr 
=-pv-qvr 
p V -q V r 
i 
h 
h 
h -(pAq) 
-(pAq) 
-(pAq) 
-(p A q) V Vr 
Vr 
Vr 
r 
= (pAq) > r. 
[Associativity 
[Associativity 
[Associativity 
[Associativity and 
and 
and 
and commutativity 
commutativity 
commutativity 
commutativity of 
of 
of 
of V] 
V] 
V] 
V] 
[p=pvp] 
[p=pvp] 
[p=pvp] 
p = p v p] 
[p > q = p v q] 
This last equivalence is a little surprising. It shows, for example, that 
if somebody says "It is either the case that if you study you will graduate 
from Yale with distinction, or that if you join the right secret society you 
will graduate from Yale with distinction", then this statement (assuming 
we treat the or as V) is logically equivalent to "If you study and join the 
right secret society, then you will graduate from Yale with distinction." It is 
easy to get tangled up in trying to parse the first of these two propositions; 
translating to logical notation and simplifying using logical equivalence is a 
good way to simplify it. 
Over the years, logicians have given names to many logical equivalences. 
Some of the more useful ones are summarized in Table 2.2. More complicated 
equivalences can often be derived from these. If that doesn't work (and you 
don't have too many variables to work with), you can always try writing out 
a truth table.

---
## Page 5

CHAPTER 2. MATHEMATICAL LOGIC 

-(pA q) = -p V -q 
-(pV q) = -p -q 
pAq =qAp 
pV q =q Vp 
pA(qAr) = (pAq) A r 
pV (qVr) = (pVq) Vr 
pA(qVr) = (pAq) V (pAr) 
pV(qAr) = (pVq) A (pVr) 
Double negation 
De Morgan's law 
De Morgan's law 
Commutativity of AND 
Commutativity of OR 
Associativity of AND 
Associativity of OR 
AND distributes over OR 
OR distributes over AND 
p \ q = -pVq 
Equivalence of implication and OR 
p \ q = -q > p 
Contraposition 
p o q = (p > q) A (q > p) 
Expansion of if and only if 
p ] q = -p o q 
Inverse of if and only f 
p ] q = q<-p 
Commutativity of if and only if 
20 
Table 2.2: Common logical equivalences (see also [Fer08, Theorem 1.1]) 

-(pA q) = -p V -q 
pV(qAr) = (pVq) A (pVr)
CHAPTER 2. MATHEMATICAL LOGIC 
M 
 
 
 
p    = p 
-(p A q) = -p V -q 
-(pVq) = □p A-q 
p \q =qp 
pV q = q V p 
p A(q A r ) = (p A q)Ar 
pV(qVr) = (pVq) Vr 
p A(qVr) = (p A q) V (p A r ) 
pV(qA r ) = (pVq)A (pVr) 
Double negation 
De Morgan's law 
De Morgan's law 
Commutativity of AND 
Commutativity of OR 
Associativity of AND 
Associativity of OR 
AND distributes over OR 
OR distributes over AND 
p N q = -pVq 
Equivalence of implication and OR 
p N q = -q > p 
Contraposition 
p O q = (p > q)A( q > p) 
Expansion of if and only if 
p O q = -po q 
Inverse of if and only f 
p O q = q<p 
Commutativity of if and only if 
20 
Table 2.2: Common logical equivalences (see also [Fer08, Theorem 1.1])
