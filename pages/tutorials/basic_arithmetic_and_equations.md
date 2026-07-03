<h1 align="center">Basic Arithmetic and Equations</h1>

Work through these tutorials after watching the [Basic Arithmetic and Equations](/math_kickstarter/basic_arithmetic_and_equations/) videos. Each subsection walks through the main ideas step by step with worked examples. The **exercises** on the topic page use different problems — they are not copies of the tutorial or video examples.

## 1. Order of operations

When an expression contains several operations, use a fixed **priority order** (often remembered as PEMDAS):

1. **Parentheses** `( )` — work inside brackets first
2. **Exponentiation** — powers such as $5^2$
3. **Multiplication** and **division** — from left to right
4. **Addition** and **subtraction** — from left to right

A **fraction bar** groups the numerator and denominator as single expressions. Evaluate the numerator and denominator separately before dividing.

**Example 1:** Evaluate $6 - 2 \times 5^2$.

1. Exponent: $5^2 = 25$
2. Multiplication: $2 \times 25 = 50$
3. Subtraction: $6 - 50 = -44$

**Example 2:** Evaluate $\dfrac{3 + 2 \times 6}{5}$.

1. Inside the numerator, multiply first: $2 \times 6 = 12$
2. Finish the numerator: $3 + 12 = 15$
3. Divide: $\dfrac{15}{5} = 3$

**Example 3:** Evaluate $(6 - 2 \times 5)^2$.

1. Inside the parentheses: $6 - 10 = -4$
2. Square: $(-4)^2 = 16$

**Example 4:** Evaluate $24 \div 4 \times 3$.

Multiplication and division have equal priority, so work **left to right**: $24 \div 4 = 6$, then $6 \times 3 = 18$.

??? tip "Check your understanding"
    Try [Exercise 1](/math_kickstarter/basic_arithmetic_and_equations/#exercise-1) on the topic page.

## 2. Fractions

A fraction $\dfrac{a}{b}$ has **numerator** $a$ (top) and **denominator** $b$ (bottom). The denominator tells you into how many equal parts a whole is divided.

**Expand or reduce** by multiplying or dividing numerator and denominator by the same non-zero number:

$$\dfrac{a}{b} = \dfrac{k \cdot a}{k \cdot b}$$

**Adding or subtracting** — denominators must match. If they do not, find a **common denominator** (often the least common multiple):

$$\dfrac{a}{b} + \dfrac{c}{d} = \dfrac{ad + bc}{bd}$$

**Multiplying** — multiply numerators and multiply denominators:

$$\dfrac{a}{b} \cdot \dfrac{c}{d} = \dfrac{ac}{bd}$$

**Dividing** — multiply by the **reciprocal** of the second fraction:

$$\dfrac{a}{b} \div \dfrac{c}{d} = \dfrac{a}{b} \cdot \dfrac{d}{c} = \dfrac{ad}{bc}$$

**Worked example:** Simplify $\dfrac{5}{6} - \dfrac{1}{4}$.

1. Common denominator of 6 and 4 is 12.
2. $\dfrac{5}{6} = \dfrac{10}{12}$ and $\dfrac{1}{4} = \dfrac{3}{12}$
3. $\dfrac{10}{12} - \dfrac{3}{12} = \dfrac{7}{12}$

**Worked example:** Simplify $\dfrac{2}{3} \div \dfrac{5}{9}$.

$$\dfrac{2}{3} \cdot \dfrac{9}{5} = \dfrac{18}{15} = \dfrac{6}{5}$$

??? tip "Check your understanding"
    Try [Exercises 2 and 9](/math_kickstarter/basic_arithmetic_and_equations/#exercise-2) on the topic page.

## 3. Exponents and radicals

**Powers:** $a^n$ means $a$ multiplied by itself $n$ times ($n > 0$).

**Laws of exponents** (same base $a \neq 0$ where needed):

| Rule | Formula |
| ---- | ------- |
| Product | $a^n \cdot a^m = a^{n+m}$ |
| Quotient | $\dfrac{a^n}{a^m} = a^{n-m}$ |
| Power of a power | $(a^n)^m = a^{nm}$ |
| Power of a product | $(a \cdot b)^n = a^n b^n$ |
| Power of a quotient | $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$ |
| Negative exponent | $a^{-n} = \dfrac{1}{a^n}$ |
| Zero exponent | $a^0 = 1$ |
| Roots and rational exponents | $\sqrt[m]{a^n} = a^{n/m}$ |

In particular, $\sqrt[n]{a} = a^{1/n}$ and $\sqrt[n]{a^m} = a^{m/n}$ (for $a \geq 0$ when $n$ is even, and where the expressions are defined).

**Square roots:** if $y^2 = x$, then $y = \pm\sqrt{x}$. The symbol $\sqrt{x}$ usually denotes the **non-negative** square root.

**Worked example:** Simplify $\dfrac{2^4 \times 2^{-2}}{2^3}$.

1. Numerator: $2^{4+(-2)} = 2^2$
2. Quotient: $\dfrac{2^2}{2^3} = 2^{2-3} = 2^{-1} = \dfrac{1}{2}$

**Worked example:** Simplify $\dfrac{x^3 \cdot x^{-5}}{x^{-2}}$.

$$\dfrac{x^{-2}}{x^{-2}} = x^0 = 1$$

**Worked example:** Evaluate $27^{\frac{1}{3}}$ using the root rule.

Using $a^{n/m} = \sqrt[m]{a^n}$ with $n = 1$ and $m = 3$:

$$27^{\frac{1}{3}} = \sqrt[3]{27} = 3$$

**Worked example:** Write $\sqrt[4]{16^3}$ as a single power.

$$\sqrt[4]{16^3} = 16^{3/4}$$

??? tip "Check your understanding"
    Try [Exercise 3](/math_kickstarter/basic_arithmetic_and_equations/#exercise-3) on the topic page.

## 4. Parentheses

**Distributive law** — multiply each term inside the bracket:

$$a(b + c) = ab + ac$$

**Adding a bracket** — the signs stay the same:

$$2r + (3 - r) = 2r + 3 - r = r + 3$$

**Subtracting a bracket** — change the sign of **every** term inside:

$$2r - (3 - r) = 2r - 3 + r = 3r - 3$$

**Special products** (learn these patterns):

| Pattern | Expansion |
| ------- | ----------- |
| $(a + b)^2$ | $a^2 + 2ab + b^2$ |
| $(a - b)^2$ | $a^2 - 2ab + b^2$ |
| $(a + b)(a - b)$ | $a^2 - b^2$ |

**Worked example:** Expand $3x + 2(x - 7)$.

$$3x + 2x - 14 = 5x - 14$$

**Worked example:** Expand $(2 + 3x)^2$.

$$(2 + 3x)^2 = 4 + 12x + 9x^2 = 9x^2 + 12x + 4$$

??? tip "Check your understanding"
    Try [Exercise 4](/math_kickstarter/basic_arithmetic_and_equations/#exercise-4) on the topic page.

## 5. Equations

The **equals sign** means the left-hand side and the right-hand side have the **same value**. It is not a signal to “write the answer next” — it states a balance.

**Rules for solving:**

- Perform the **same operation on both sides** of the equation
- You may simplify either side, as long as its value does not change
- Aim to **collect variable terms** on one side and numbers on the other

**Worked example:** Solve $4x - 2 = 18 - x$.

1. Add $x$ to both sides: $5x - 2 = 18$
2. Add 2 to both sides: $5x = 20$
3. Divide by 5: $x = 4$

**Worked example:** Solve $\dfrac{2z + 3}{2} = z + 4$.

1. Multiply both sides by 2: $2z + 3 = 2z + 8$
2. Subtract $2z$ from both sides: $3 = 8$

This is never true, so there is **no solution**.

**Worked example:** Solve $\dfrac{3(x - 2)}{4} - \dfrac{2(x + 1)}{3} = 1$.

1. Multiply through by 12 (LCM of 4 and 3): $9(x - 2) - 8(x + 1) = 12$
2. Expand: $9x - 18 - 8x - 8 = 12$
3. Simplify: $x - 26 = 12$, so $x = 38$

Substituting back confirms the solution.

??? tip "Check your understanding"
    Try [Exercises 5 and 10](/math_kickstarter/basic_arithmetic_and_equations/#exercise-5) on the topic page.

## 6. Quadratic equations

A **quadratic equation** in **standard form** is

$$ax^2 + bx + c = 0 \quad (a \neq 0)$$

Before using the quadratic formula, **expand and simplify** until the equation is in this form. In this course, use the **quadratic formula** as the standard method once the equation is in standard form (factoring is not required here).

**Quadratic formula:**

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

The **discriminant** is $\Delta = b^2 - 4ac$:

| Discriminant | Real solutions |
| ------------ | -------------- |
| $\Delta > 0$ | Two distinct real solutions |
| $\Delta = 0$ | One repeated real solution |
| $\Delta < 0$ | No real solutions |

**Worked example:** Solve $2x^2 - 4x - 6 = 0$ using the quadratic formula.

1. Identify coefficients: $a = 2$, $b = -4$, $c = -6$
2. Discriminant: $\Delta = (-4)^2 - 4(2)(-6) = 16 + 48 = 64$
3. Apply the formula:
   $x = \frac{-(-4) \pm \sqrt{64}}{2(2)} = \frac{4 \pm 8}{4}$
4. Two solutions: $x = \dfrac{12}{4} = 3$ or $x = \dfrac{-4}{4} = -1$

**Worked example:** Solve $4x(x + 1) + 3 = 2$ using the quadratic formula.

1. Expand and write in standard form: $4x^2 + 4x + 1 = 0$, so $a = 4$, $b = 4$, $c = 1$
2. Discriminant: $\Delta = 4^2 - 4(4)(1) = 16 - 16 = 0$
3. Apply the formula:
   $x = \frac{-4 \pm \sqrt{0}}{2(4)} = \frac{-4}{8} = -\dfrac{1}{2}$
4. One repeated solution: $x = -\dfrac{1}{2}$

**Worked example:** Use the discriminant and quadratic formula for $x^2 + 6x + 9 = 0$.

1. Here $a = 1$, $b = 6$, $c = 9$, so $\Delta = 36 - 36 = 0$ (one real solution)
2. $$x = \frac{-6 \pm \sqrt{0}}{2} = \frac{-6}{2} = -3$$

**Worked example:** For $3x^2 - 2x + 5 = 0$, $\Delta = (-2)^2 - 4(3)(5) = 4 - 60 = -56 < 0$, so the quadratic formula gives no **real** solutions ($\sqrt{-56}$ is not a real number).

??? tip "Check your understanding"
    Try [Exercises 6 and 7](/math_kickstarter/basic_arithmetic_and_equations/#exercise-6) on the topic page.

## 7. Rearranging formulae

To make a variable the **subject** of a formula, treat the formula like an equation and **undo operations in reverse order** (inverse operations).

**Strategy:**

1. Identify the **structure**: sums, products, powers, and parentheses
2. Decide which variable to isolate
3. Undo operations starting with the one **furthest from** that variable
4. Apply the same operation to **both sides** at each step

**Worked example:** Make $r$ the subject of $V = \dfrac{4}{3}\pi r^3$.

1. Divide both sides by $\dfrac{4}{3}\pi$: $r^3 = \dfrac{3V}{4\pi}$
2. Take the cube root: $r = \sqrt[3]{\dfrac{3V}{4\pi}}$

**Worked example:** Make $r$ the subject of $A = P(1 + r)^t$.

1. Divide by $P$: $\dfrac{A}{P} = (1 + r)^t$
2. Take the $t$th root: $1 + r = \left(\dfrac{A}{P}\right)^{1/t}$
3. Subtract 1: $r = \left(\dfrac{A}{P}\right)^{1/t} - 1$

**Key idea:** rearranging uses the same balance rules as solving equations — only the variable you want to isolate is treated as unknown; all other letters are constants for that step.

??? tip "Check your understanding"
    Try [Exercise 8](/math_kickstarter/basic_arithmetic_and_equations/#exercise-8) on the topic page.
