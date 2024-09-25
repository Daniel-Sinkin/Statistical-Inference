# Theorem 4.2.6
Let $(X, Y)$ be a discrete bivaraite random vector with joint pmf $f_{X, Y}(x, y)$. Then the marginal pmfs of $X$ and $Y$, $f_X(x) = P(X = x)$ and $f_Y(y) = P(Y = y)$, are given by
$$
\begin{aligned}
f_X(x) = \sum_{y \in \mathbb{R}} f_{X, Y}(x, y),&&f_Y(y) = \sum_{x \in \mathbb{R}} f_{X, Y}(x, y).
\end{aligned}
$$

## Proof Sketch
Let $A_x := \{x\} \times \mathbb{R}$ be the line that crosses $x$ perpendicularly, we just have to show that $f_X(x) = f_{X, Y}((X, Y) \in A_x).$