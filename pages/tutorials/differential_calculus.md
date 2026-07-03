<h1 align="center">Differential Calculus</h1>

Work through these tutorials after watching the [Differential Calculus](/math_kickstarter/differential_calculus/) videos. Each subsection walks through the main ideas step by step with worked examples. The **exercises** on the topic page use different problems — they are not copies of the tutorial or video examples.

## 1. Derivatives and tangents

A function can be **increasing** (as $x$ increases, $y$ increases) or **decreasing** (as $x$ increases, $y$ decreases). Often the **rate of change** itself changes along the graph.

The **tangent line** at a point on a graph is the straight line that touches the curve and matches its slope at that point. Because a tangent is a line $y = ax + b$, its **slope** $a$ gives a number for the instantaneous rate of change.

### From secant to derivative

Pick a point $(x_0, f(x_0))$ and a nearby point. The line through them is a **secant**. Its slope is

$$\frac{\Delta y}{\Delta x}$$

As the second point moves closer ( $\Delta x \to 0$ ), the secant approaches the tangent. The **derivative** is this limiting slope:

$$f'(x) = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}$$

In practice we use differentiation **rules** rather than evaluating the limit each time.

### Notation

The derivative of $f(x)$ can be written as:

- $f'(x)$
- $\dfrac{df}{dx}$ or $\dfrac{d}{dx}f(x)$

### What the derivative tells you

| Sign of $f'(x)$ | Meaning |
| --------------- | ------- |
| $f'(x) > 0$ | $f$ is **increasing** at $x$ |
| $f'(x) < 0$ | $f$ is **decreasing** at $x$ |
| $f'(x) = 0$ | horizontal tangent — possible **local maximum** or **local minimum** |

**Summary:** $f'(x)$ is the slope of the tangent at $x$, and it measures the rate of change of $f$ at that point.

??? tip "Check your understanding"
    Try [Exercises 7 and 8](/math_kickstarter/differential_calculus/#exercise-7) on the topic page.

## 2. Differentiation rules

This topic covers **basic** rules only. The product rule, quotient rule, and chain rule are **not** included here.

### Simple rules

| Rule | Formula |
| ---- | ------- |
| Sum | $(f + g)' = f' + g'$ |
| Difference | $(f - g)' = f' - g'$ |
| Constant multiple | $(c \cdot f)' = c \cdot f'$ |

Differentiate **term by term**. Constants differentiate to $0$.

### Common derivatives

| Function $f(x)$ | Derivative $f'(x)$ |
| --------------- | ------------------ |
| $c$ (constant) | $0$ |
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $\ln x$ | $\dfrac{1}{x}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |

**Power rule:** $\dfrac{d}{dx}(x^n) = nx^{n-1}$. This also works for negative exponents, e.g. $\dfrac{1}{x^2} = x^{-2}$.

**Worked example:** Differentiate $f(x) = \dfrac{1}{2}x^4 + 2x^3 - x^2 + x - 7$.

Differentiate each term:

$$f'(x) = 2x^3 + 6x^2 - 2x + 1$$

**Worked example:** Differentiate $f(x) = \dfrac{1}{x^2} + \ln x - \cos x$.

Rewrite $\dfrac{1}{x^2} = x^{-2}$:

$$f'(x) = -2x^{-3} + \dfrac{1}{x} + \sin x$$

**Worked example — find a minimum:** For $f(x) = 3e^x - 6x$, find where $f'(x) = 0$.

$$f'(x) = 3e^x - 6$$

Set $f'(x) = 0$:

$$3e^x = 6 \;\Rightarrow\; e^x = 2 \;\Rightarrow\; x = \ln 2 \approx 0.693$$

At a minimum the tangent is horizontal, so $f'(x) = 0$. To confirm it is a minimum (not a maximum), check that $f'$ is negative to the left of $x = \ln 2$ and positive to the right — or sketch the graph.

The minimum value is:

$$f(\ln 2) = 3e^{\ln 2} - 6\ln 2 = 6 - 6\ln 2 \approx 1.84$$

??? tip "Check your understanding"
    Try [Exercises 1, 2, 9, and 10](/math_kickstarter/differential_calculus/#exercise-1) on the topic page.
