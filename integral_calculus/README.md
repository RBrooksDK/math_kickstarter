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

<style>
body[data-md-color-scheme] .md-content ol       { list-style-type: lower-alpha; }
body[data-md-color-scheme] .md-content ol li    { padding-left: 10px; }
</style>

#### Exercise 1

Evaluate:

1. $\int (3x^2 + 2) \, dx$
2. $\int_0^2 x \, dx$

??? answer "&nbsp;"

    1. $x^3 + 2x + C$
    2. $2$

#### Exercise 2

Evaluate $\int (x^3 - 5x + 4) \, dx$.

??? answer "&nbsp;"

    $\dfrac{x^4}{4} - \dfrac{5x^2}{2} + 4x + C$

#### Exercise 3

Evaluate $\int \dfrac{2}{x} \, dx$.

??? answer "&nbsp;"

    $2\ln|x| + C$

#### Exercise 4

Evaluate $\int (3\cos x - \sin x) \, dx$.

??? answer "&nbsp;"

    $3\sin x + \cos x + C$

#### Exercise 5

Evaluate $\displaystyle\int_1^4 (2x + 1) \, dx$.

??? answer "&nbsp;"

    An antiderivative is $x^2 + x$, so $[x^2 + x]_1^4 = (16 + 4) - (1 + 1) = 18$.

#### Exercise 6

Evaluate $\displaystyle\int_0^{\pi/2} \sin x \, dx$.

??? answer "&nbsp;"

    $[-\cos x]_0^{\pi/2} = (-\cos(\pi/2)) - (-\cos 0) = 0 - (-1) = 1$.

#### Exercise 7

Evaluate $\displaystyle\int_{-1}^1 x \, dx$ and explain the result in terms of signed area.

??? answer "&nbsp;"

    $\left[\dfrac{x^2}{2}\right]_{-1}^1 = \dfrac{1}{2} - \dfrac{1}{2} = 0$. The graph of $y = x$ lies below the axis on $[-1, 0]$ and above on $[0, 1]$; equal areas with opposite signs cancel.

#### Exercise 8

Find the area between the graph of $f(x) = x^2$ and the $x$-axis from $x = 0$ to $x = 3$.

??? answer "&nbsp;"

    $\displaystyle\int_0^3 x^2 \, dx = \left[\dfrac{x^3}{3}\right]_0^3 = 9$. Since $x^2 \geq 0$ on $[0, 3]$, the integral equals the geometric area.

#### Exercise 9

Verify that $F(x) = x^3 + 2x$ is an antiderivative of $f(x) = 3x^2 + 2$ by differentiating $F$, then evaluate $\displaystyle\int_0^1 (3x^2 + 2) \, dx$.

??? answer "&nbsp;"

    $F'(x) = 3x^2 + 2 = f(x)$, so $F$ is an antiderivative. $\displaystyle\int_0^1 (3x^2 + 2) \, dx = F(1) - F(0) = (1 + 2) - 0 = 3$.

#### Exercise 10

A velocity function is $v(t) = 3t^2 - 2$ (in m/s). Find the displacement from $t = 0$ to $t = 2$ seconds.

??? answer "&nbsp;"

    Displacement $= \displaystyle\int_0^2 (3t^2 - 2) \, dt = [t^3 - 2t]_0^2 = (8 - 4) - 0 = 4$ m.
