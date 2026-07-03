<h1 align="center">Vectors in 2D</h1>

Work through the videos below in order. When you have watched them, take the quiz and try the exercises. A quiz score of at least **7 out of 10** suggests sufficient understanding.

<hr>

## Learning objectives

After working through this topic, you should be able to:

- Represent vectors in the coordinate plane and perform vector algebra
- Compute the dot product of two vectors and interpret the result
- Use parametric equations to describe a line in 2D *(optional)*

<hr>

## Videos

### 1. Vectors in 2D

Distinguish vectors from scalars, write vectors in component form, and add, subtract, and scale them.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; overflow: hidden;">
    <iframe
        src="https://drive.google.com/file/d/1ipNlX3n3EZaH4iO42k4oH8SLFwV18seh/preview"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        allow="autoplay; encrypted-media"
        allowfullscreen>
    </iframe>
</div>

### 2. Dot product

Compute the dot product, find vector length, and determine angles between vectors.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; overflow: hidden;">
    <iframe
        src="https://drive.google.com/file/d/1DiNWMjw4dWUUYTUZwzmVk6zxJU7HSv4v/preview"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        allow="autoplay; encrypted-media"
        allowfullscreen>
    </iframe>
</div>

### 3. Parametric equation of a line *(optional)*

Describe a line in the plane using a position vector, a direction vector, and a parameter.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; overflow: hidden;">
    <iframe
        src="https://drive.google.com/file/d/1M8AtJvYEMEKRcU3r7w1DcCheqn8AH2cP/preview"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        allow="autoplay; encrypted-media"
        allowfullscreen>
    </iframe>
</div>

<hr>

## Quiz

When you have been through the videos, test your understanding with the quiz below. The quiz contains 10 questions. A score of at least **7 out of 10** suggests sufficient understanding. You can see your total score at the bottom of the page, as well as your score for each question. You can retake the quiz as many times as you like — results are not stored or assessed.

<?quiz?>
question: Which of the following is a vector quantity?
answer: Speed
answer-correct: Displacement
answer: Mass
answer: Temperature
content:
<p><strong>Explanation:</strong> A vector has both magnitude and direction. Displacement specifies how far and in which direction something moves; speed, mass, and temperature are scalars (magnitude only).</p>
<?/quiz?>

---

<?quiz?>
question: Which notation correctly represents a vector with horizontal component $3$ and vertical component $-2$?
answer: $3 - 2$
answer-correct: $(3, -2)$
answer: $|3, -2|$
answer: $3 \times (-2)$
content:
<p><strong>Explanation:</strong> In component notation, a 2D vector is written as an ordered pair $(x, y)$ giving the horizontal and vertical components.</p>
<?/quiz?>

---

<?quiz?>
question: If $\mathbf{u} = (1, 2)$ and $\mathbf{v} = (4, -1)$, what is $\mathbf{u} + \mathbf{v}$?
answer: $(5, 3)$
answer-correct: $(5, 1)$
answer: $(4, 2)$
answer: $(1, -1)$
content:
<p><strong>Explanation:</strong> Add components: $(1 + 4,\; 2 + (-1)) = (5, 1)$.</p>
<?/quiz?>

---

<?quiz?>
question: If $\mathbf{u} = (5, 3)$ and $\mathbf{v} = (2, 1)$, what is $\mathbf{u} - \mathbf{v}$?
answer: $(7, 4)$
answer-correct: $(3, 2)$
answer: $(3, 4)$
answer: $(2, 2)$
content:
<p><strong>Explanation:</strong> Subtract components: $(5 - 2,\; 3 - 1) = (3, 2)$.</p>
<?/quiz?>

---

<?quiz?>
question: What is $3\mathbf{a}$ when $\mathbf{a} = (2, -4)$?
answer: $(5, -1)$
answer-correct: $(6, -12)$
answer: $(6, -4)$
answer: $(2, -12)$
content:
<p><strong>Explanation:</strong> Multiply each component by the scalar: $3(2, -4) = (6, -12)$.</p>
<?/quiz?>

---

<?quiz?>
question: What is the dot product $\mathbf{a} \cdot \mathbf{b}$ for $\mathbf{a} = (2, 3)$ and $\mathbf{b} = (4, 1)$?
answer: 8
answer-correct: 11
answer: 14
answer: 5
content:
<p><strong>Explanation:</strong> $\mathbf{a} \cdot \mathbf{b} = a_x b_x + a_y b_y = 2 \cdot 4 + 3 \cdot 1 = 8 + 3 = 11$.</p>
<?/quiz?>

---

<?quiz?>
question: What is the length $|\mathbf{a}|$ of $\mathbf{a} = (3, 4)$?
answer: $7$
answer-correct: $5$
answer: $25$
answer: $\sqrt{7}$
content:
<p><strong>Explanation:</strong> $|\mathbf{a}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.</p>
<?/quiz?>

---

<?quiz?>
question: If $\theta$ is the angle between nonzero vectors $\mathbf{a}$ and $\mathbf{b}$, which expression equals $\cos\theta$?
answer: $\dfrac{|\mathbf{a}| |\mathbf{b}|}{\mathbf{a} \cdot \mathbf{b}}$
answer-correct: $\dfrac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}| |\mathbf{b}|}$
answer: $\mathbf{a} \cdot \mathbf{b}$
answer: $\dfrac{|\mathbf{a}| + |\mathbf{b}|}{\mathbf{a} \cdot \mathbf{b}}$
content:
<p><strong>Explanation:</strong> The dot product formula is $\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos\theta$, so $\cos\theta = \dfrac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}| |\mathbf{b}|}$.</p>
<?/quiz?>

---

<?quiz?>
question: Vectors $\mathbf{u} = (1, 2)$ and $\mathbf{v} = (4, -2)$ are perpendicular. Why?
answer: Because $|\mathbf{u}| = |\mathbf{v}|$
answer-correct: Because $\mathbf{u} \cdot \mathbf{v} = 0$
answer: Because their components are equal
answer: Because $\mathbf{u} + \mathbf{v} = \mathbf{0}$
content:
<p><strong>Explanation:</strong> Two nonzero vectors are perpendicular when their dot product is zero: $\mathbf{u} \cdot \mathbf{v} = 1 \cdot 4 + 2 \cdot (-2) = 4 - 4 = 0$.</p>
<?/quiz?>

---

<?quiz?>
question: A line is given by $\mathbf{r} = \mathbf{r}_0 + t\mathbf{d}$ with $\mathbf{r}_0 = (1, 2)$ and $\mathbf{d} = (3, 1)$. What is the position vector when $t = 2$?
answer: $(4, 3)$
answer-correct: $(7, 4)$
answer: $(5, 3)$
answer: $(6, 2)$
content:
<p><strong>Explanation:</strong> $\mathbf{r} = (1, 2) + 2(3, 1) = (1 + 6,\; 2 + 2) = (7, 4)$.</p>
<?/quiz?>

<hr>

## Exercises

<style>
body[data-md-color-scheme] .md-content ol       { list-style-type: lower-alpha; }
body[data-md-color-scheme] .md-content ol li    { padding-left: 10px; }
</style>

#### Exercise 1

Given $\mathbf{u} = (4, -1)$ and $\mathbf{v} = (1, 5)$, find:

1. $\mathbf{u} + \mathbf{v}$
2. $\mathbf{u} - \mathbf{v}$
3. $3\mathbf{u}$

??? answer "&nbsp;"

    1. $(5, 4)$
    2. $(3, -6)$
    3. $(12, -3)$

#### Exercise 2

Given $\mathbf{a} = (2, 4)$ and $\mathbf{b} = (3, -2)$, compute $\mathbf{a} \cdot \mathbf{b}$.

??? answer "&nbsp;"

    $\mathbf{a} \cdot \mathbf{b} = 2 \cdot 3 + 4 \cdot (-2) = 6 - 8 = -2$

#### Exercise 3

Find the length $|\mathbf{c}|$ when $\mathbf{c} = (6, 8)$.

??? answer "&nbsp;"

    $|\mathbf{c}| = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$

#### Exercise 4

Find $\cos\theta$ for the angle $\theta$ between $\mathbf{a} = (3, 0)$ and $\mathbf{b} = (0, 4)$.

??? answer "&nbsp;"

    $\mathbf{a} \cdot \mathbf{b} = 0$, $|\mathbf{a}| = 3$, and $|\mathbf{b}| = 4$, so $\cos\theta = 0$. The vectors are perpendicular.

#### Exercise 5

Are $\mathbf{u} = (1, 4)$ and $\mathbf{v} = (8, -2)$ perpendicular? Justify your answer.

??? answer "&nbsp;"

    Yes. $\mathbf{u} \cdot \mathbf{v} = 1 \cdot 8 + 4 \cdot (-2) = 8 - 8 = 0$, so the vectors are perpendicular.

#### Exercise 6

Find the value of $k$ such that $\mathbf{a} = (2, k)$ and $\mathbf{b} = (3, 1)$ satisfy $\mathbf{a} \cdot \mathbf{b} = 10$.

??? answer "&nbsp;"

    $2 \cdot 3 + k \cdot 1 = 10 \;\Rightarrow\; 6 + k = 10 \;\Rightarrow\; k = 4$

#### Exercise 7

Given $\mathbf{a} = (3, 1)$ and $\mathbf{b} = (1, 2)$, find $2\mathbf{a} - \mathbf{b}$.

??? answer "&nbsp;"

    $2(3, 1) - (1, 2) = (6, 2) - (1, 2) = (5, 0)$

#### Exercise 8

A line passes through the origin with direction vector $\mathbf{d} = (1, 4)$. Using $\mathbf{r} = t\mathbf{d}$, find the point on the line when $t = 3$.

??? answer "&nbsp;"

    $\mathbf{r} = 3(1, 4) = (3, 12)$

#### Exercise 9 *(optional)*

A line is given by $\mathbf{r} = (2, 1) + t(2, 3)$. Find the position vector when $t = 2$.

??? answer "&nbsp;"

    $\mathbf{r} = (2, 1) + 2(2, 3) = (2 + 4,\; 1 + 6) = (6, 7)$

#### Exercise 10

Given $\mathbf{a} = (4, 1)$ and $\mathbf{b} = (1, 2)$, find $|\mathbf{a} + \mathbf{b}|$.

??? answer "&nbsp;"

    $\mathbf{a} + \mathbf{b} = (5, 3)$, so $|\mathbf{a} + \mathbf{b}| = \sqrt{5^2 + 3^2} = \sqrt{25 + 9} = \sqrt{34}$
