import matplotlib.pyplot as plt
import numpy as np


def plot_exponential(lambda_: float) -> None:
    xs = np.arange(0.0, 4.0, 0.15)
    ys = (1.0 / lambda_) * np.exp(-xs / lambda_)

    (line,) = plt.plot(
        xs,
        ys,
        marker="*",
        label=f"lambda = {lambda_:.2f}",
    )
    plt.axvline(
        x=lambda_,
        color=line.get_color(),
        ls="--",
    )


def main() -> None:
    lambdas = [0.5, 1.0, 4.0]
    for lambda_ in lambdas:
        plot_exponential(lambda_)
    plt.title("Exponential Distribution\nDashed line is Expectation")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
