# COT3541 Propositional Logic Lecture Notes Week 1-1.docx

> Source: `inbox/COT3541 Propositional Logic Lecture Notes Week 1-1.docx` · type: docx · ~2263 words · extracted 2026-10-24 13:00

## Chapter 2 - Propositional Logic

Symbols	Connectives (∨, ∧, →, ↔, ¬, 0, 1)
variables

### 2.1 Propositional Connectives, Propositional Formulas, And Truth Tables

Propositional logic started to appear about twenty-five years after Boole's work with the calculus of classes. The idea was simply that one could work with basic units called propositions, each of which was true or false. However, this viewpoint did not become the dominant one, replacing the logic of classes, until Whitehead and Russell's Principia Mathematica appeared in the years 1910-1913.

We assume the reader is as comfortable with the concept of a proposition as with the concepts of points, lines, and natural numbers. Nonetheless, it seems worthwhile to repeat that a proposition is a statement that is true or false. We can modify or connect such propositions with connectives like not, and, or, implies, and iff to form other propositions. Propositions are a key ingredient in correct arguments, in law as well as in mathematics. The object of propositional logic is to study general principles regarding the notion of correct argument.

To obtain general principles we work with propositional variables  rather than with particular propositions. We will use the letter  for our set of propositional variables. To make the notation more concise we introduce the following symbols for the standard connectives, including the standard constants:

To say that  is a connective is somewhat of an abuse of terminology, since we apply it to a single proposition, and the constants do not connect anything. But it is simpler to refer to the collection of seven symbols as the set of connectives.

In propositional logic the connectives not, and, or, etc., will be used as in mathematics, e.g., we say  holds if at least one of ,  holds.

#### 2.1.1 Defining Propositional Formulas

If we combine propositional variables in a meaningful way with these symbols we obtain propositional formulas, e.g.,

Although this description of propositional formulas by example may be quite clear to some readers, we still want to give a mathematically precise definition of what is meant by a propositional formula. Our goal is to give an inductive definition, that is, to initially describe some strings of symbols that we will call formulas and then to give a procedure to create new formulas from ones that we already have. All the strings of symbols that we can obtain in this manner, and only in this manner, will constitute our collection of propositional formulas. [This parallels the inductive description of the natural numbers, namely, starting with 0, and given any natural number , its successor is also a natural number.]

The propositional formulas in the standard connectives are (inductively) defined by the following statements:

Each propositional variable is a propositional formula.

0 and 1 are propositional formulas.

If  is a propositional formula, then  is a propositional formula.

If  and  are propositional formulas, then , (  ), and (  ) are propositional formulas.

The propositional formulas are precisely the strings of symbols that we can make using the listed statements.

Notational Convention 2.1.1 In practice we often like to drop the outer parentheses in a formula for readability, putting them back in when we want to use them as part of a larger formula, e.g., , but .

Remark 2.1.2 We are using infix notation for the binary connectives. If we used prefix notation, e.g.,  instead of , then we would be able to dispense with parentheses, e.g.,  instead of . If we choose to use prefix notation, then we need to convince ourselves that the parentheses are not needed, i.e., that we have unique readability of prefix notation.

Notational Convention 2.1.3 In algebra we know that  means  and not . This is because we have agreed on this convention to make algebraic formulas more readable. Likewise, to make propositional formulas more readable, we adopt precedence conventions for the standard connectives, namely:

Figure 2.1.4 Precedence convention

Higher connectives in this figure have greater binding power, but we will need parentheses to determine the precedence for those on the same level. For example,  means , but  is ambiguous. We need to know if  or  is correct.

When discussing propositional formulas we will, on occasion, refer to certain components called subformulas.

Definition 2.1.5 The subformulas of a formula  are defined inductively by the following conditions:

The only subformula of a propositional variable  is  itself.

The only subformula of a constant  is  itself (  is 0 or 1 ).

The subformulas of  are , and all subformulas of .

The subformulas of G ◻ H are G ◻ H and all subformulas of G and all subformulas of H , where ◻ denotes any of the four binary connectives .

Example 2.1.6 The subformulas of  are .

Remark 2.1.7 A brief summary of how to write up inductive definitions over formulas is given in Appendix C.

#### 2.1.2 Truth Tables

A formula by itself is not true or false-it becomes so only after the propositional variables are replaced with concrete propositions. To determine whether such a concrete instantiation is true or false one needs to know the impact of the connectives on truth values as determined by the standard truth tables:

|  |  |
|---|---|
| 1 | 0 |
| 0 | 1 |

|  |  |  |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 0 |

|  |  |  |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | 0 |

|  |  |  |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 1 |
| 0 | 0 | 1 |

|  |  |  |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 1 |

One can easily justify the choice of truth values in all the tables but the one for "implies."

is true iff  is false.

is true iff both  and  are true.

is true iff at least one of  or  is true.

is true iff  and  are both true, or both false.

The truth table for  has been a longstanding source of doubt and irritation. If  is true, then of course  is true iff  is true. That takes care of two of the rows of the truth table, the ones with a 1 in the  column. But the dubious part is to say that  is always true when  is false. A statement like "If the moon is made of yellow cheese, then I am the Prince of Denmark" would be true by this definition, a statement to which one is perhaps not so ready to assign a truth value.

One way out of this problem with the meaning of "implies" is to agree that  expresses the same thing as . Indeed, this is how we use the word "implies" in mathematics. Thus the statement above becomes "Either the moon is not made of yellow cheese or I am the Prince of Denmark," which is transparently true. With this agreement on the use of "implies" the truth table for  is easily seen to be as shown.

Now. given any propositional formula  we have a truth table for F, e.g., for  we have

|  |  |  |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 1 |

A longer version of the truth table includes the truth tables for the subformulas:

|  |  |  |  |  |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 0 |
| 0 | 0 | 0 | 0 | 1 |

Definition 2.1.8 A truth evaluation  for the list  of propositional variables is a sequence of  truth values. Given a formula  let  denote the propositional formula  obtained by replacing each  by , and let  be the truth value of  when the connectives are evaluated according to their truth tables.

Example 2.1.9 Let  be the formula

and let e be the truth evaluation  for . Then  is the propositional formula , and by carrying out the truth table calculations on this expression, we see that .

Notational Convention 2.1.10 If F is a propositional formula, then we use the notation  to indicate that the variables occurring in F are among the variables . It is not necessary for all these variables to occur in .

Example 2.1.11 Let  be the propositional formula  . Note that only the variables  and  actually occur in the formula.

If  is a propositional formula and e is a truth evaluation for , then

|  |  |  |  |
|---|---|---|---|

gives a row of the truth table of . Furthermore, each row of the truth table of F comes from some truth evaluation e. Therefore, truth evaluations correspond to individual lines of truth lables.

### Exercises

2.1.1 Fill in the following truth tables:

a.

|  |  |  |  |  |
|---|---|---|---|---|
| 1 | 1 |  |  |  |
| 1 | 0 |  |  |  |
| 0 | 1 |  |  |  |
| 0 | 0 |  |  |  |

b.

|  |  |  |  |  |
|---|---|---|---|---|
| 1 | 1 |  |  |  |
| 1 | 0 |  |  |  |
| 0 | 1 |  |  |  |
| 0 | 0 |  |  |  |

c.

|  |  |  |  |
|---|---|---|---|
| 1 | 1 |  |  |
| 1 | 0 |  |  |
| 0 | 1 |  |  |
| 0 | 0 |  |  |

d.

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| 1 | 1 |  |  |  |  |
| 1 | 0 |  |  |  |  |
| 0 | 1 |  |  |  |  |
| 0 | 0 |  |  |  |  |

e.

|  |  |  |  |  |
|---|---|---|---|---|
| 1 | 1 | 1 |  |  |
| 1 | 1 | 0 |  |  |
| 1 | 0 | 1 |  |  |
| 1 | 0 | 0 |  |  |
| 0 | 1 | 1 |  |  |
| 0 | 1 | 0 |  |  |
| 0 | 0 | 1 |  |  |
| 0 | 0 | 0 |  |  |

f.

|  |  |  |  |  |
|---|---|---|---|---|
| 1 | 1 | 1 |  |  |
| 1 | 1 | 0 |  |  |
| 1 | 0 | 1 |  |  |
| 1 | 0 | 0 |  |  |
| 0 | 1 | 1 |  |  |
| 0 | 1 | 0 |  |  |
| 0 | 0 | 1 |  |  |
| 0 | 0 | 0 |  |  |

### 2.2 Equivalent Formulas, Tautologies, And Contradictions

There are many different ways to say the same thing in our propositional logic. This fact motivates the notion of equivalent formulas.

#### 2.2.1 Equivalent Formulas

Definition 2.2.1 We will say that two propositional formulas  and  are (truth) equivalent, written , if  for every truth evaluation e for the variables, i.e, if they have the same truth tables (using tables with enough variables to include all the variables appearing in either formula).

Proposition 2.2.2

Proof. Just look at the truth tables.

We have just expressed the standard connectives in terms of  (insofar as truth equivalence is concerned). Thus as far as expressive power is concerned, the two connectives  are all we really need to build propositional formulas.

The following is a very useful list of equivalent formulas.

#### Theorem 2.2.3 [Fundamental Truth Equivalences]

|  | Equivalent statements | Equivalent statements | Equivalent statements | Law/property |
|---|---|---|---|---|
| 1. |  |  |  | idempotent |
| 2. |  |  |  | idempotent |
| 3. |  |  |  | commutative |
| 4. |  |  |  | commutative |
| 5. |  |  |  | associative |
| 6. |  |  |  | associative |
| 7. |  |  |  | absorption |
| 8. |  |  |  | absorption |
| 9. |  |  |  | distributive |
| 10. |  |  |  | distributive |
| 11. |  |  | 1 | excluded middle |
| 12. |  |  | 0 |  |
| 13. |  |  |  |  |
| 14. |  |  | 1 |  |
| 15. |  |  |  |  |
| 16. |  |  |  |  |
| 17. |  |  | 0 |  |
| 18. |  |  |  | DeMorgan's law |
| 19. |  |  |  | DeMorgan's law |
| 20. |  |  |  |  |
| 21. |  |  |  |  |
| 22. |  |  |  |  |
| 23. |  |  |  |  |
| 24. |  |  | 1 |  |
| 25. |  |  |  |  |
| 26. |  |  |  |  |
| 27. |  |  |  |  |
| 28. |  |  |  |  |
| 29. |  |  |  |  |
| 30. |  |  |  |  |
| 31. |  |  |  |  |

Proof. (Exercise.)
