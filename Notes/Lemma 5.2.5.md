# Lemma 5.2.5
Let $X_1, \dots, X_n$ be a random sample from a population and let $g(x)$ be a function such that $Eg(X_1)$ and $\text{Var} g(X_1)$ exist. Then

$$
E\left( \sum_{i=1}^{n} g(X_i) \right) = n \cdot E(g(X_1))
\tag{5.2.1}
$$

and

$$
\text{Var} \left( \sum_{i=1}^{n} g(X_i) \right) = n \cdot \text{Var} g(X_1)
\tag{5.2.2}
$$

## Proof Notes
Let $\mu = E[g(X_1)]$, by definition of a sample we have $\mu = E[g(X_i)]$ for all $i$, similiarly
$$
\sigma^2 := \operatorname{Var}(g(X_1)) = E[(g(X_1) - \mu)^2] = \operatorname{Var}(g(X_i))
$$
for all $i$.

The proof boils down to expanding $\operatorname{Var}\left(\sum_{i = 1}^ g(X_i)\right)$, and applying Theorem 4.5.5 which implies
$$
E[(g(X_i) - \mu)(g(X_j) - \mu)] = \operatorname{Cov}(g(X_i), g(X_j)) = 0.
$$