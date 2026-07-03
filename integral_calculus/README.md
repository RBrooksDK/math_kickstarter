<h1 align="center">Integral Calculus</h1>

Work through the videos below in order. When you have watched them, take the quiz and try the exercises. A quiz score of at least **7 out of 10** suggests sufficient understanding.

<hr>

## Learning objectives

After working through this topic, you should be able to:

- Find indefinite integrals (antiderivatives) of simple functions
- Evaluate definite integrals
- Interpret definite integrals as area under a curve
- Apply basic integration techniques only (no substitution or partial fractions)

<hr>

## Videos

### 1. Indefinite integrals and antiderivatives

Find antiderivatives and evaluate basic indefinite integrals, including the constant of integration.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; overflow: hidden;">
    <iframe
        src="https://drive.google.com/file/d/1OT5ozJAPbSRzQXCRqwdF3UPd89Q7TPuA/preview"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        allow="autoplay; encrypted-media"
        allowfullscreen>
    </iframe>
</div>

### 2. Definite integrals and areas

Evaluate definite integrals and interpret them as signed area under a curve.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; overflow: hidden;">
    <iframe
        src="https://drive.google.com/file/d/15MMVoyBq_taQUXt_wfuh7av91EwzDfBL/preview"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        allow="autoplay; encrypted-media"
        allowfullscreen>
    </iframe>
</div>

<hr>

## Quiz

When you have been through the videos, test your understanding with the quiz below. The quiz contains 10 questions. A score of at least **7 out of 10** suggests sufficient understanding. You can see your total score at the bottom of the page, as well as your score for each question. You can retake the quiz as many times as you like — results are not stored or assessed.

<?quiz?>
question: What is $\int 2x \, dx$?
answer: $2x^2 + C$
answer-correct: $x^2 + C$
answer: $x^2$
answer: $2 + C$
content:
<p><strong>Explanation:</strong> An antiderivative of $2x$ is $x^2$, so $\int 2x \, dx = x^2 + C$.</p>
<?/quiz?>

---

<?quiz?>
question: If $F'(x) = f(x)$, what do we call $F$?
answer: A derivative of $f$
answer-correct: An antiderivative of $f$
answer: The slope of $f$
answer: The definite integral of $f$
content:
<p><strong>Explanation:</strong> An antiderivative (or indefinite integral) of $f$ is a function $F$ whose derivative equals $f$.</p>
<?/quiz?>

---

<?quiz?>
question: Why do we write $+C$ after an indefinite integral?
answer: Because every integral equals zero
answer-correct: Because antiderivatives are only unique up to an additive constant
answer: Because $C$ is always the value at $x = 0$
answer: Because the integral sign requires it for notation only
content:
<p><strong>Explanation:</strong> If $F'(x) = f(x)$, then so does $(F + C)'(x)$ for any constant $C$. The $+C$ captures every possible antiderivative.</p>
<?/quiz?>

---

<?quiz?>
question: What is $\int x^4 \, dx$?
answer: $4x^3 + C$
answer-correct: $\dfrac{x^5}{5} + C$
answer: $5x^4 + C$
answer: $\dfrac{x^4}{4} + C$
content:
<p><strong>Explanation:</strong> Reverse the power rule: $\int x^n \, dx = \dfrac{x^{n+1}}{n+1} + C$ for $n \neq -1$, so $\int x^4 \, dx = \dfrac{x^5}{5} + C$.</p>
<?/quiz?>

---

<?quiz?>
question: What is $\int \dfrac{1}{x} \, dx$?
answer: $x^{-2} + C$
answer-correct: $\ln|x| + C$
answer: $e^x + C$
answer: $-\dfrac{1}{x^2} + C$
content:
<p><strong>Explanation:</strong> The antiderivative of $\dfrac{1}{x}$ is the natural logarithm: $\int \dfrac{1}{x} \, dx = \ln|x| + C$ (for $x \neq 0$).</p>
<?/quiz?>

---

<?quiz?>
question: What is $\int \cos x \, dx$?
answer: $-\sin x + C$
answer-correct: $\sin x + C$
answer: $\cos x + C$
answer: $-\cos x + C$
content:
<p><strong>Explanation:</strong> Since $\dfrac{d}{dx}(\sin x) = \cos x$, we have $\int \cos x \, dx = \sin x + C$.</p>
<?/quiz?>

---

<?quiz?>
question: If $F'(x) = f(x)$, how is the definite integral $\displaystyle\int_a^b f(x)\, dx$ evaluated?
answer: $F(a) - F(b)$
answer-correct: $F(b) - F(a)$
answer: $f(b) - f(a)$
answer: $F(b) + F(a)$
content:
<p><strong>Explanation:</strong> The Fundamental Theorem of Calculus gives $\displaystyle\int_a^b f(x)\, dx = F(b) - F(a)$, where $F$ is any antiderivative of $f$.</p>
<?/quiz?>

---

<?quiz?>
question: What is $\displaystyle\int_0^3 2x \, dx$?
answer: $6$
answer-correct: $9$
answer: $3$
answer: $18$
content:
<p><strong>Explanation:</strong> An antiderivative of $2x$ is $x^2$, so $\displaystyle\int_0^3 2x \, dx = [x^2]_0^3 = 9 - 0 = 9$.</p>
<?/quiz?>

---

<?quiz?>
question: When a function is below the $x$-axis on an interval, how does the definite integral relate to the geometric area?
answer: The integral equals the area exactly
answer-correct: The integral is negative, giving a signed area
answer: The integral is always zero
answer: The integral cannot be computed
content:
<p><strong>Explanation:</strong> Definite integrals measure signed area: regions above the axis contribute positively and regions below contribute negatively.</p>
<?/quiz?>

---

<?quiz?>
question: What is $\int (3x^2 - 4x + 1) \, dx$?
answer: $6x - 4 + C$
answer-correct: $x^3 - 2x^2 + x + C$
answer: $x^3 - 2x^2 + C$
answer: $3x^3 - 4x^2 + x + C$
content:
<p><strong>Explanation:</strong> Integrate term by term: $\int 3x^2 \, dx = x^3$, $\int -4x \, dx = -2x^2$, and $\int 1 \, dx = x$, giving $x^3 - 2x^2 + x + C$.</p>
<?/quiz?>

<hr>

## Exercises

For step-by-step worked examples and formulas for this topic, see the [Integral Calculus tutorial](/math_kickstarter/pages/tutorials/integral_calculus/).

<style>
body[data-md-color-scheme] .md-content ol       { list-style-type: lower-alpha; }
body[data-md-color-scheme] .md-content ol li    { padding-left: 10px; }
</style>

#### Exercise 1

Evaluate:

1. $\int (5x^2 + 1) \, dx$
2. $\displaystyle\int_0^3 3x \, dx$

??? answer "&nbsp;"

    1. $\dfrac{5x^3}{3} + x + C$
    2. $\left[\dfrac{3x^2}{2}\right]_0^3 = \dfrac{27}{2}$

#### Exercise 2

Evaluate $\int (x^4 - 2x^2 + 3) \, dx$.

??? answer "&nbsp;"

    $\dfrac{x^5}{5} - \dfrac{2x^3}{3} + 3x + C$

#### Exercise 3

Evaluate $\int \dfrac{4}{x} \, dx$.

??? answer "&nbsp;"

    $4\ln|x| + C$

#### Exercise 4

Evaluate $\int (2\cos x + 4\sin x) \, dx$.

??? answer "&nbsp;"

    $2\sin x - 4\cos x + C$

#### Exercise 5

Evaluate $\displaystyle\int_2^5 (3x + 2) \, dx$.

??? answer "&nbsp;"

    An antiderivative is $\dfrac{3x^2}{2} + 2x$, so $\left[\dfrac{3x^2}{2} + 2x\right]_2^5 = \left(\dfrac{75}{2} + 10\right) - (6 + 4) = \dfrac{75}{2}$.

#### Exercise 6

Evaluate $\displaystyle\int_0^{\pi/2} \cos x \, dx$.

??? answer "&nbsp;"

    $[\sin x]_0^{\pi/2} = 1 - 0 = 1$.

#### Exercise 7

Evaluate $\displaystyle\int_{-2}^2 2x \, dx$ and explain the result in terms of signed area.

??? answer "&nbsp;"

    $\left[x^2\right]_{-2}^2 = 4 - 4 = 0$. The graph of $y = 2x$ lies below the axis on $[-2, 0]$ and above on $[0, 2]$; equal signed areas cancel.

#### Exercise 8

Find the area between the graph of $f(x) = x^2$ and the $x$-axis from $x = 0$ to $x = 2$.

??? answer "&nbsp;"

    $\displaystyle\int_0^2 x^2 \, dx = \left[\dfrac{x^3}{3}\right]_0^2 = \dfrac{8}{3}$. Since $x^2 \geq 0$ on $[0, 2]$, the integral equals the geometric area.

#### Exercise 9

Verify that $F(x) = \dfrac{x^3}{3} + 4x$ is an antiderivative of $f(x) = x^2 + 4$ by differentiating $F$, then evaluate $\displaystyle\int_0^1 (x^2 + 4) \, dx$.

??? answer "&nbsp;"

    $F'(x) = x^2 + 4 = f(x)$, so $F$ is an antiderivative. $\displaystyle\int_0^1 (x^2 + 4) \, dx = F(1) - F(0) = \left(\dfrac{1}{3} + 4\right) - 0 = \dfrac{13}{3}$.

#### Exercise 10

A velocity function is $v(t) = t^2 + 1$ (in m/s). Find the displacement from $t = 0$ to $t = 3$ seconds.

??? answer "&nbsp;"

    Displacement $= \displaystyle\int_0^3 (t^2 + 1) \, dt = \left[\dfrac{t^3}{3} + t\right]_0^3 = (9 + 3) - 0 = 12$ m.
