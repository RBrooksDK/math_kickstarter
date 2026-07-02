<h1 align="center">Differential Calculus</h1>

Work through the videos below in order. When you have watched them, take the quiz and try the exercises. A quiz score of at least **7 out of 10** suggests sufficient understanding.

<hr>

## Learning objectives

After working through this topic, you should be able to:

- Interpret the derivative as the slope of a tangent line
- Differentiate simple power functions and common expressions
- Apply basic differentiation rules (this topic does **not** cover product, quotient, or chain rule)

<hr>

## Videos

### 1. Derivatives and tangents

Interpret the derivative as the slope of a tangent and as a rate of change.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; overflow: hidden;">
    <iframe
        src="https://drive.google.com/file/d/1n-fOBmgzvXej-MS5IRVL2FHOCuZTCr18/preview"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        allow="autoplay; encrypted-media"
        allowfullscreen>
    </iframe>
</div>

### 2. Differentiation rules

Differentiate sums, differences, and constant multiples, and use common derivative formulas.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; overflow: hidden;">
    <iframe
        src="https://drive.google.com/file/d/1oxDdX00962-xaWQwqzbvQ9d1DGuldaZq/preview"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        allow="autoplay; encrypted-media"
        allowfullscreen>
    </iframe>
</div>

<hr>

## Quiz

When you have been through the videos, test your understanding with the quiz below. The quiz contains 10 questions. A score of at least **7 out of 10** suggests sufficient understanding. You can see your total score at the bottom of the page, as well as your score for each question. You can retake the quiz as many times as you like — results are not stored or assessed.

<?quiz?>
question: What is the derivative of $f(x) = x^3$?
answer: $3x$
answer-correct: $3x^2$
answer: $x^2$
answer: $3x^3$
content:
<p><strong>Explanation:</strong> Using the power rule, $\dfrac{d}{dx}(x^n) = nx^{n-1}$, so $\dfrac{d}{dx}(x^3) = 3x^2$.</p>
<?/quiz?>

---

<?quiz?>
question: Geometrically, what does $f'(a)$ represent at a point on the graph of $f$?
answer: The $y$-coordinate of the point $(a, f(a))$
answer-correct: The slope of the tangent line to the graph at $x = a$
answer: The area under the graph from $0$ to $a$
answer: The average slope of the graph over the interval $[0, a]$
content:
<p><strong>Explanation:</strong> The derivative at a point gives the instantaneous rate of change of $f$, which equals the slope of the tangent line at that point.</p>
<?/quiz?>

---

<?quiz?>
question: If $f'(x) > 0$ for all $x$ in an interval, what can we conclude about $f$ on that interval?
answer: $f$ is decreasing
answer-correct: $f$ is increasing
answer: $f$ has a local maximum
answer: $f$ is constant
content:
<p><strong>Explanation:</strong> A positive derivative means the function's output is rising as $x$ increases, so $f$ is increasing on that interval.</p>
<?/quiz?>

---

<?quiz?>
question: At a local maximum of a differentiable function $f$, what must be true about $f'(x)$ at that point?
answer: $f'(x) = 1$
answer-correct: $f'(x) = 0$
answer: $f'(x)$ is undefined
answer: $f'(x) < 0$
content:
<p><strong>Explanation:</strong> At a local maximum the tangent line is horizontal, so the slope — and hence the derivative — is zero.</p>
<?/quiz?>

---

<?quiz?>
question: What is $\dfrac{d}{dx}(e^x)$?
answer: $xe^{x-1}$
answer-correct: $e^x$
answer: $\dfrac{1}{x}$
answer: $e$
content:
<p><strong>Explanation:</strong> The exponential function $e^x$ is its own derivative: $\dfrac{d}{dx}(e^x) = e^x$.</p>
<?/quiz?>

---

<?quiz?>
question: What is $\dfrac{d}{dx}(\ln x)$?
answer: $e^x$
answer-correct: $\dfrac{1}{x}$
answer: $x$
answer: $\ln x$
content:
<p><strong>Explanation:</strong> The derivative of the natural logarithm is $\dfrac{d}{dx}(\ln x) = \dfrac{1}{x}$ (for $x > 0$).</p>
<?/quiz?>

---

<?quiz?>
question: What is $\dfrac{d}{dx}(\sin x)$?
answer: $-\sin x$
answer-correct: $\cos x$
answer: $-\cos x$
answer: $\sin x$
content:
<p><strong>Explanation:</strong> Differentiating sine gives cosine: $\dfrac{d}{dx}(\sin x) = \cos x$.</p>
<?/quiz?>

---

<?quiz?>
question: What is $\dfrac{d}{dx}(4x^2 - 3x + 7)$?
answer: $4x - 3$
answer-correct: $8x - 3$
answer: $8x^2 - 3$
answer: $4x^2 - 3$
content:
<p><strong>Explanation:</strong> Apply the sum/difference and constant-multiple rules together with the power rule: $\dfrac{d}{dx}(4x^2) = 8x$, $\dfrac{d}{dx}(-3x) = -3$, and the derivative of the constant $7$ is $0$.</p>
<?/quiz?>

---

<?quiz?>
question: Which of the following is **not** covered in this topic?
answer: The constant multiple rule
answer-correct: The chain rule
answer: The power rule for $x^n$
answer: The derivative of $\cos x$
content:
<p><strong>Explanation:</strong> This topic covers basic rules and common derivatives only. The product rule, quotient rule, and chain rule are left for later study.</p>
<?/quiz?>

---

<?quiz?>
question: Using the constant multiple rule, what is $\dfrac{d}{dx}(5\sin x)$?
answer: $5\cos x + C$
answer-correct: $5\cos x$
answer: $\sin(5x)$
answer: $5\sin x$
content:
<p><strong>Explanation:</strong> The constant multiple rule gives $\dfrac{d}{dx}(5\sin x) = 5 \cdot \dfrac{d}{dx}(\sin x) = 5\cos x$. Note that $+C$ belongs to integration, not differentiation.</p>
<?/quiz?>

<hr>

## Exercises

<style>
body[data-md-color-scheme] .md-content ol       { list-style-type: lower-alpha; }
body[data-md-color-scheme] .md-content ol li    { padding-left: 10px; }
</style>

#### Exercise 1

Differentiate the following:

1. $f(x) = 5x^4$
2. $f(x) = 3x^2 + 2x - 7$

??? answer "&nbsp;"

    1. $f'(x) = 20x^3$
    2. $f'(x) = 6x + 2$

#### Exercise 2

Differentiate $f(x) = x^5 - 4x^3 + x$.

??? answer "&nbsp;"

    $f'(x) = 5x^4 - 12x^2 + 1$

#### Exercise 3

Differentiate $f(x) = e^x + 6$.

??? answer "&nbsp;"

    $f'(x) = e^x$

#### Exercise 4

Differentiate $f(x) = \ln x$.

??? answer "&nbsp;"

    $f'(x) = \dfrac{1}{x}$

#### Exercise 5

Differentiate $f(x) = \sin x + \cos x$.

??? answer "&nbsp;"

    $f'(x) = \cos x - \sin x$

#### Exercise 6

Differentiate $f(x) = 2\sin x - 3\cos x + e^x$.

??? answer "&nbsp;"

    $f'(x) = 2\cos x + 3\sin x + e^x$

#### Exercise 7

Find the value(s) of $x$ where $f'(x) = 0$ for $f(x) = x^2 - 4x + 3$.

??? answer "&nbsp;"

    $f'(x) = 2x - 4$, so $2x - 4 = 0$ gives $x = 2$.

#### Exercise 8

For $f(x) = -x^2 + 6x$, find $f'(x)$ and state whether $f$ is increasing or decreasing at $x = 1$.

??? answer "&nbsp;"

    $f'(x) = -2x + 6$. At $x = 1$, $f'(1) = 4 > 0$, so $f$ is increasing at $x = 1$.

#### Exercise 9

Differentiate $f(x) = \dfrac{3}{x} + x^2$ (write $\dfrac{3}{x}$ as $3x^{-1}$ first).

??? answer "&nbsp;"

    $f(x) = 3x^{-1} + x^2$, so $f'(x) = -3x^{-2} + 2x = -\dfrac{3}{x^2} + 2x$.

#### Exercise 10

The graph of $f(x) = x^3 - 3x$ has a local maximum and a local minimum. Find where $f'(x) = 0$ and state which value of $x$ gives the local maximum.

??? answer "&nbsp;"

    $f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 3(x-1)(x+1)$, so $f'(x) = 0$ at $x = -1$ and $x = 1$. Evaluating: $f(-1) = 2$ and $f(1) = -2$, so the local maximum occurs at $x = -1$.
