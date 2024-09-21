Suppose $X \sim \operatorname{Bin}(n, p)$ i.e.
$$
f_X(x) = \binom{n}{x}p^x(1 - p)^{n - x}
$$
and consider $g(x) := n - x$ then we obtain a new random variable by
$$
Y := g(X) = n - x.
$$
We want to compute the distribution, to do this we note that $g(x) = y$ is equivalent to $y = n - x$, i.e. $g^{-1}(y) = n - y$, with that we can compute
$$
f_Y(y) = \sum_{x \in g^{-1}(\{y\})} f_X(x) = f_X(n - x) = ... = \binom{n}{y}(1 - p)^y p^{n - y}.
$$