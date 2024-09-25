# Theorem 4.2.12
Let $X$ and $Y$ be independent random variables with moment generating functions $M_X(t)$ and $M_Y(t)$. Then the moment generating function of the random variable $Z = X + Y$ is given by
$$
M_Z(t) = M_X(t)M_Y(t)
$$

## Proof
Using Theorem 4.2.10 we can compute:
$$
M_Z(t) = E\left[e^{tZ}\right] = E\left[e^{t(X + Y)}\right] = E[e^{tX}e^{tY}] = E\left[e^{tX}\right] \cdot E\left[e^{tY}\right] = M_X(t) M_Y(t).
$$