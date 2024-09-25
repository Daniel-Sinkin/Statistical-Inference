# Theorem 4.2.10
Let $X$ and $Y$ be independent random variables.
1. For any $A \subseteq \mathbb{R}$ and $B \subseteq \mathbb{R}, P(X \in A, Y \in B) = P(X \in A)P(Y\in B)$; that is the events $\{X \in A\}$ and $\{Y \in B\}$ are independent events.
2. Let $g(x)$ be a function only of $x$ and $h(y)$ be a function only of $y$. Then
3. $$E[g(X)h(Y)] = E[g(X)] \cdot E[h(Y)]$$

## Proof Sketch
By definition $X$ and $Y$ are called independent if
$$
f(x, y) = f_X(x)f_Y(y),
$$
using this we can split the integral / sum for $E[g(X)h(Y)]$ into a product.

The first part follows from the observation that for indicator functions the following identity holds
$$
1_A(x) \cdot 1_B(y) = 1 \iff I(x, y)  = 1
$$
where $I$ is the indicator function of $\{(x, y) : x \in A, y \in B\}$.