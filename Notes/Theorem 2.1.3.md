# Statement
Let $X$ have cdf $F_X(x)$, let $Y = g(X)$, and let $\mathcal{X}$ and $\mathcal{Y}$ be defined as in (2.1.7).
* If $g$ is an increasing function on $\mathcal{X}$ then $F_Y(y) = F_X(g^{-1}(y))$ for $y \in \mathcal{Y}$.
* If $g$ is a decreasing function on $\mathcal{X}$ and $X$ is a continuous random variable then $F_Y(y) = 1 - F_X(g^{-1}(y))$.

# Proof (Sketch)
Follows immediately from
$$
\{x \in \mathcal{X} : g(x) \leq y\} = \{x \in \mathcal{X} : g^{-1}(g(x)) \leq g^{-1}(y)\} = \{x \in \mathcal{X} : x \leq g^{-1}(y)\}
$$
in the monotone increasing case and
$$
\{x \in \mathcal{X} : g(x) \leq y\} = \{x \in \mathcal{X} : g^{-1}(g(x)) \leq g^{-1}(y)\} = \{x \in \mathcal{X} : x \geq g^{-1}(y)\}
$$
in the monotone decreasing case.
