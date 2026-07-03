<h1 align="center">Vectors in 2D</h1>

Work through these tutorials after watching the [Vectors in 2D](/math_kickstarter/vectors/) videos. Each subsection walks through the main ideas step by step with worked examples. The **exercises** on the topic page use different problems — they are not copies of the tutorial or video examples.

## 1. Vectors in 2D

A **vector** has both **magnitude** (length) and **direction**. A **scalar** has only a value (no direction).

| | Vector | Scalar |
| --- | --- | --- |
| Has direction? | Yes | No |
| Examples | velocity, force, displacement | speed, mass, temperature |

Vectors are drawn as arrows. We write $\vec{a}$ (arrow over the letter) to show it is a vector, or use **bold** $\mathbf{a}$ in printed text. Sometimes a bar, $\bar{a}$, is used instead, but the arrow $\vec{a}$ is the standard notation for vectors. Here we use $\mathbf{a}$ for vectors.

### Component form

A 2D vector can be written as an ordered pair:

$$\mathbf{a} = (a_1, a_2)$$

where $a_1$ is the horizontal component and $a_2$ is the vertical component.

**Worked example:** Draw $\mathbf{a} = (-1, 3)$.

<p align="center">
  <img src="/math_kickstarter/figures/vector_a_minus1_3.png" alt="Vector a = (-1, 3) from the origin" />
</p>

From the origin: one step left ($-1$), then three steps up ($3$). The dashed lines show the horizontal and vertical components. The same vector can be drawn anywhere — only magnitude and direction matter.

### Scaling

Multiply each component by the scalar $c$:

$$c\mathbf{a} = (ca_1,\; ca_2)$$

- $c > 1$ stretches the vector
- $0 < c < 1$ shortens it
- $c = -1$ reverses direction ($-\mathbf{a}$)

**Worked example:** If $\mathbf{a} = (-1, 3)$, find $3\mathbf{a}$ and $-\mathbf{a}$.

$$3\mathbf{a} = (-3, 9), \qquad -\mathbf{a} = (1, -3)$$

### Addition and subtraction

Add or subtract **component by component**:

$$\mathbf{a} + \mathbf{b} = (a_1 + b_1,\; a_2 + b_2)$$

$$\mathbf{a} - \mathbf{b} = (a_1 - b_1,\; a_2 - b_2)$$

Geometrically, place vectors tip-to-tail (or use the parallelogram rule). Note that $\mathbf{a} - \mathbf{b} = \mathbf{a} + (-\mathbf{b})$.

**Worked example:** With $\mathbf{a} = (-1, 3)$ and $\mathbf{b} = (4, 3)$:

$$\mathbf{a} + \mathbf{b} = (3, 6), \qquad \mathbf{a} - \mathbf{b} = (-5, 0)$$

??? tip "Check your understanding"
    Try [Exercise 1](/math_kickstarter/vectors/#exercise-1) and [Exercise 7](/math_kickstarter/vectors/#exercise-7) on the topic page.

## 2. Dot product

The **dot product** (also called scalar product) of $\mathbf{a} = (a_1, a_2)$ and $\mathbf{b} = (b_1, b_2)$ is:

$$\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2$$

The result is a **scalar**, not a vector.

**Worked example:** For $\mathbf{a} = (-3, 4)$ and $\mathbf{b} = (1, 2)$:

$$\mathbf{a} \cdot \mathbf{b} = (-3)(1) + (4)(2) = -3 + 8 = 5$$

### Length of a vector

$$|\mathbf{a}|^2 = \mathbf{a} \cdot \mathbf{a} = a_1^2 + a_2^2, \qquad |\mathbf{a}| = \sqrt{a_1^2 + a_2^2}$$

This is the Pythagorean theorem applied to the components.

**Worked example:** For $\mathbf{a} = (-3, 4)$:

$$|\mathbf{a}| = \sqrt{(-3)^2 + 4^2} = \sqrt{9 + 16} = 5$$

### Angle between vectors

$$\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}|\,|\mathbf{b}|\cos\theta$$

So (when both vectors are nonzero):

$$\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}|\,|\mathbf{b}|}$$

**Worked example — perpendicular vectors:** For $\mathbf{a} = (6, -2)$ and $\mathbf{b} = \left(\dfrac{1}{3}, 1\right)$:

$$\mathbf{a} \cdot \mathbf{b} = 6 \cdot \frac{1}{3} + (-2)(1) = 2 - 2 = 0$$

So $\cos\theta = 0$ and $\theta = 90°$. The vectors are **orthogonal** (perpendicular). We write $\mathbf{a} \perp \mathbf{b}$.

### Projection

The projection of $\mathbf{a}$ onto $\mathbf{b}$ is the component of $\mathbf{a}$ in the direction of $\mathbf{b}$:

$$\text{proj}_{\mathbf{b}}(\mathbf{a}) = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{b}|^2}\,\mathbf{b}$$

**Worked example:** For $\mathbf{a} = (2, 8)$ and $\mathbf{b} = (8, 2)$:

$$\mathbf{a} \cdot \mathbf{b} = 16 + 16 = 32, \qquad |\mathbf{b}|^2 = 64 + 4 = 68$$

$$\text{proj}_{\mathbf{b}}(\mathbf{a}) = \frac{32}{68}\,\mathbf{b} = \frac{8}{17}\,\mathbf{b}$$

??? tip "Check your understanding"
    Try [Exercises 2, 3, 4, and 5](/math_kickstarter/vectors/#exercise-2) on the topic page.

## 3. Parametric equation of a line

A point $P_0$ with position vector $\mathbf{r}_0$ and a **direction vector** $\mathbf{d}$ determine a line. The parameter $t$ controls how far we move along $\mathbf{d}$:

$$\mathbf{r} = \mathbf{r}_0 + t\mathbf{d}$$

As $t$ ranges over all real numbers, $\mathbf{r}$ traces every point on the line.

In components, with $\mathbf{r}_0 = (x_0, y_0)$ and $\mathbf{d} = (d_1, d_2)$:

$$x = x_0 + t d_1, \qquad y = y_0 + t d_2$$

The same line can be described in many ways (different starting points or direction vectors).

**Worked example:** A line through $(3, 0)$ with direction $(3, 2)$:

$$\mathbf{r} = (3, 0) + t(3, 2)$$

When $t = 10$:

$$\mathbf{r} = (3 + 30,\; 0 + 20) = (33, 20)$$

**Worked example — parallel line:** Through $(2, 4)$ with the same direction $(3, 2)$:

$$\mathbf{r} = (2, 4) + t(3, 2)$$

**Worked example — orthogonal line:** A direction vector orthogonal to $(3, 2)$ satisfies $3d_1 + 2d_2 = 0$. One choice is $\mathbf{d} = (-2, 3)$. A line through $(3, 0)$:

$$\mathbf{r} = (3, 0) + t(-2, 3)$$

??? tip "Check your understanding"
    Try [Exercises 8, 9, and 10](/math_kickstarter/vectors/#exercise-8) on the topic page.
