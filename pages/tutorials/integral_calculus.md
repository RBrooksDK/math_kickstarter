<h1 align="center">Integral Calculus</h1>

Work through these tutorials after watching the [Integral Calculus](/math_kickstarter/integral_calculus/) videos. Each subsection walks through the main ideas step by step with worked examples. The **exercises** on the topic page use different problems — they are not copies of the tutorial or video examples.

## 1. Indefinite integrals and antiderivatives

Differentiation finds the **rate of change** $f(x) = F'(x)$. Integration reverses this process.

If $F'(x) = f(x)$, then $F$ is an **antiderivative** of $f$. We often use a **capital letter** for antiderivatives.

**Example:** For $f(x) = 2x$, one antiderivative is $F(x) = x^2$, because $\dfrac{d}{dx}(x^2) = 2x$.

Adding any constant also works: $x^2 + 73$ is still an antiderivative of $2x$, since the derivative of a constant is $0$.

The **indefinite integral** collects all antiderivatives:

$$\int f(x)\, dx = F(x) + C$$

Always include **$dx$** (the variable of integration) and **$+C$** (the arbitrary constant).

### Rules for indefinite integrals

| Rule | Formula |
| ---- | ------- |
| Sum | $\int (f + g)\, dx = \int f\, dx + \int g\, dx$ |
| Difference | $\int (f - g)\, dx = \int f\, dx - \int g\, dx$ |
| Constant multiple | $\int c \cdot f\, dx = c \int f\, dx$ |

Integrate **term by term**. This topic does **not** cover substitution or partial fractions.

### Common antiderivatives

| Function $f(x)$ | Antiderivative $\int f(x)\, dx$ |
| --------------- | -------------------------------- |
| $c$ (constant) | $cx + C$ |
| $x^n$ ($n \ne -1$) | $\dfrac{x^{n+1}}{n+1} + C$ |
| $e^x$ | $e^x + C$ |
| $\dfrac{1}{x}$ | $\ln\lvert x\rvert + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |

**Power rule for integration:** add 1 to the exponent, then divide by the new exponent.

**Worked example:** Evaluate $\int (x^3 + x^2)\, dx$.

$$\int x^3\, dx + \int x^2\, dx = \frac{x^4}{4} + \frac{x^3}{3} + C$$

**Worked example:** Evaluate $\int \left(\dfrac{1}{x^2} + 3x - \sin x\right) dx$.

Rewrite $\dfrac{1}{x^2} = x^{-2}$:

$$\int x^{-2}\, dx + 3\int x\, dx - \int \sin x\, dx = -\frac{1}{x} + \frac{3x^2}{2} + \cos x + C$$

**Worked example:** Evaluate $\int (2x^3 - 7)\, dx$ and check by differentiating.

$$\int 2x^3\, dx - \int 7\, dx = \frac{1}{2}x^4 - 7x + C$$

Check: $\dfrac{d}{dx}\left(\dfrac{1}{2}x^4 - 7x + C\right) = 2x^3 - 7$ ✓

??? tip "Check your understanding"
    Try [Exercises 1, 2, 3, and 4](/math_kickstarter/integral_calculus/#exercise-1) on the topic page.

## 2. Definite integrals and areas

A **definite integral** from $a$ to $b$ gives the **signed area** between the graph of $f$ and the $x$-axis on $[a, b]$:

- Area **above** the axis counts as **positive**
- Area **below** the axis counts as **negative**

### Fundamental Theorem of Calculus

If $F'(x) = f(x)$, then

$$\int_a^b f(x)\, dx = F(b) - F(a)$$

Any antiderivative works — the constant $C$ cancels in the difference. Usually choose $C = 0$.

**Notation:** $\displaystyle\left[F(x)\right]_a^b = F(b) - F(a)$

| Type | Result |
| ---- | ------ |
| Indefinite integral $\int f(x)\, dx$ | A **family of functions** ($+ C$) |
| Definite integral $\int_a^b f(x)\, dx$ | A **number** (signed area) |

**Worked example — area under a line:** Find $\displaystyle\int_0^5 (x - 2)\, dx$.

An antiderivative is $F(x) = \dfrac{x^2}{2} - 2x$:

$$\left[\frac{x^2}{2} - 2x\right]_0^5 = \left(\frac{25}{2} - 10\right) - 0 = 2.5$$

The graph crosses the $x$-axis at $x = 2$; regions above and below the axis combine to give signed area $2.5$.

**Worked example — signed area:** Evaluate $\displaystyle\int_{-1}^1 (6x^2 - 4)\, dx$.

$$F(x) = 2x^3 - 4x$$

$$F(1) - F(-1) = (2 - 4) - (-2 + 4) = -2 - 2 = -4$$

The negative result reflects more area below the axis than above on $[-1, 1]$.

**Worked example:** Evaluate $\displaystyle\int_0^{\pi} \sin x\, dx$.

An antiderivative is $-\cos x$:

$$\left[-\cos x\right]_0^{\pi} = (-\cos\pi) - (-\cos 0) = -(-1) - (-1) = 1 + 1 = 2$$

??? tip "Check your understanding"
    Try [Exercises 5, 6, 7, 8, and 10](/math_kickstarter/integral_calculus/#exercise-5) on the topic page.
