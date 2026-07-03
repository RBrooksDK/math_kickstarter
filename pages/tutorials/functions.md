<h1 align="center">Functions</h1>

Work through these tutorials after watching the [Functions](/math_kickstarter/functions/) videos. Each subsection walks through the main ideas step by step with worked examples. The **exercises** on the topic page use different problems — they are not copies of the tutorial or video examples.

## 1. Functions and graphs

A **function** takes an **input** and returns exactly one **output**. We often write the input as $x$ and the output as $y = f(x)$.

| Term | Meaning |
| ---- | ------- |
| **Domain** | All input values $x$ for which the function is defined |
| **Range** | All possible output values $f(x)$ |

**Key property:** one input cannot give two different outputs. Different inputs may give the same output.

A function can be represented by a **formula**, a **table**, a **graph**, or a **word description**. In calculations we usually prefer a formula.

### Function notation

In $f(x) = 2x + 3$:

- $f$ is the **name** of the function
- $x$ is the **variable** (input)
- $f(x)$ is the **output value** when the input is $x$

**Worked example — evaluate:** Find $f(5)$ when $f(x) = 2x + 3$.

Substitute $x = 5$: $f(5) = 2(5) + 3 = 13$.

**Worked example — solve:** If $f(x) = 5$ and $f(x) = 2x + 3$, find $x$.

Here $5$ is an **output**, not “$x = 5$”. Solve:

$$2x + 3 = 5 \;\Rightarrow\; 2x = 2 \;\Rightarrow\; x = 1$$

**Worked example — domain and range:** For $f(x) = \sqrt{2x}$, find the domain and range.

- $\sqrt{2x}$ requires $2x \ge 0$, so **domain** is $[0, \infty)$.
- Square roots are non-negative, so **range** is $[0, \infty)$.

**Worked example — reading a graph:** The graph of $f(x) = \sqrt{2x}$ passes through $(8, 4)$.

<p align="center">
  <img src="/math_kickstarter/figures/function_sqrt_2x.png" alt="Graph of f(x) = sqrt(2x) showing f(8) = 4 and f(x) = 5 at x = 12.5" />
</p>

That means $f(8) = 4$.

To find the input when the output is $5$, use the graph (or solve $\sqrt{2x} = 5$):

$$2x = 25 \;\Rightarrow\; x = 12.5$$

So when $f(x) = 5$, the input is $12.5$.

??? tip "Check your understanding"
    Try [Exercise 1](/math_kickstarter/functions/#exercise-1) and [Exercise 5](/math_kickstarter/functions/#exercise-5) on the topic page.

## 2. Common function types

### Linear functions

$$f(x) = ax + b$$

- $a$ is the **slope** (rate of change)
- $b$ is the **$y$-intercept**

Linear growth has a **constant** rate of change: increasing $x$ by 1 always changes $y$ by $a$.

**Worked example:** From the graph of a line with slope $2$ and $y$-intercept $-1$, write the formula.

$$f(x) = 2x - 1$$

### Power functions

$$f(x) = b x^a \qquad (x > 0 \text{ when needed for non-integer } a)$$

- $b = f(1)$ (value at $x = 1$)
- The exponent $a$ controls shape:
  - $a < 0$: decreasing
  - $0 < a < 1$: increasing, but flattening
  - $a > 1$: increasing, getting steeper

For power functions, a percentage change in $x$ leads to a predictable percentage change in $y$ (multiply $x$ by $k$, multiply $y$ by $k^a$).

**Worked example:** Three power functions all pass through $(1, 2)$, so $b = 2$ for each. Examples include $f(x) = 2x^{-1}$, $f(x) = 2x^{0.5}$, and $f(x) = 2x^2$ — same $b$, different $a$.

### Exponential functions

$$f(x) = b \cdot a^x \qquad (a > 0,\; a \ne 1)$$

- $b$ is the **initial value** ($f(0) = b$)
- $a$ is the **growth factor**
  - $0 < a < 1$: decreasing (each step multiplies by $a$)
  - $a > 1$: increasing

**Worked example:** $f(x) = 2 \cdot 0.4^x$ has $b = 2$ and $a = 0.4$. Each time $x$ increases by 1, the value is multiplied by $0.4$ (a decrease of 60%).

**Worked example:** $f(x) = 2 \cdot 1.6^x$ has $b = 2$ and $a = 1.6$. Each time $x$ increases by 1, the value increases by 60%.

Exponential functions have a rate of change **proportional** to the current value — the graph gets steeper as $y$ grows.

??? tip "Check your understanding"
    Try [Exercises 2 and 3](/math_kickstarter/functions/#exercise-2) on the topic page.

## 3. Inverse functions

The **inverse function** $f^{-1}$ reverses $f$: if $f(x) = y$, then $f^{-1}(y) = x$.

An inverse exists only when $f$ is **one-to-one** (each output comes from exactly one input). Use the **horizontal line test**: if some horizontal line hits the graph more than once, there is no inverse on that domain.

**Example:** $f(x) = x^2$ is not one-to-one on all real numbers (both $2$ and $-2$ give output $4$). Restricting to $x \ge 0$ allows $\sqrt{x}$ as the inverse.

### Finding an inverse algebraically

1. Write $y = f(x)$
2. Swap $x$ and $y$
3. Solve for $y$
4. Write the result as $f^{-1}(x)$

**Worked example:** Find the inverse of $g(x) = 3x + 2$.

1. $y = 3x + 2$
2. Swap: $x = 3y + 2$
3. Solve: $y = \dfrac{x - 2}{3}$
4. So $g^{-1}(x) = \dfrac{x - 2}{3}$

The graphs of $f$ and $f^{-1}$ are **reflections** of each other in the line $y = x$.

### Logarithms as inverses of exponentials

If $f(x) = 10^x$, then $f^{-1}(x) = \log_{10}(x)$.

| $x$ | $10^x$ | $\log_{10}(x)$ |
| --- | ------ | -------------- |
| 0 | 1 | — |
| 1 | 10 | 0 |
| 2 | 100 | 1 |
| 3 | 1000 | 2 |

So $\log_{10}(1000) = 3$ because $10^3 = 1000$.

Similarly, $f(x) = e^x$ has inverse $f^{-1}(x) = \ln(x)$ (natural logarithm), where $e \approx 2.718$.

Useful facts:

- $e^0 = 1$, so $\ln(1) = 0$
- $\ln(x)$ is defined only for $x > 0$ (you cannot take $\ln(0)$)

**Worked example:** Simplify $\log_{10}(10^x)$.

Since $\log_{10}$ undoes $10^x$, the result is $x$ (for $x > 0$ in the inner exponential when working with real logarithms in applied settings).

??? tip "Check your understanding"
    Try [Exercises 6, 8, and 10](/math_kickstarter/functions/#exercise-6) on the topic page.
