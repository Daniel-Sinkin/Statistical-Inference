import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def plot_sin_squared_with_sublevel_set():
    """
    This function plots y = sin^2(x) and highlights the sub level set where y <= 0.6 in light pink.
    It also shades rectangles formed between the points where y = 0.6, with a weak horizontal line
    added at y = 0.6.
    """
    x = np.linspace(0, 2 * np.pi, 500)
    y = np.sin(x) ** 2

    initial_guesses = [1, 2, 4, 5]
    x_solutions = fsolve(lambda x: np.sin(x) ** 2 - 0.6, initial_guesses)
    x1, x2, x3, x4 = x_solutions

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=r'$y = \sin^2(x)$')
    plt.fill_between(x, y, 0, where=(y <= 0.6), color='lightpink', alpha=1.0)
    plt.fill_betweenx([0, 0.6], x1, x2, color='lightpink', alpha=1.0)
    plt.fill_betweenx([0, 0.6], x3, x4, color='lightpink', alpha=1.0)
    plt.axhline(0.6, color='gray', linestyle='--', linewidth=0.5)

    xticks = [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]
    xtick_labels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
    plt.xticks(xticks, labels=xtick_labels)

    plt.title(r'Plot of $y = \sin^2(x)$ with Shaded sub level Set $ \leq 0.6$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(False)
    plt.show()

if __name__ == "__main__":
    plot_sin_squared_with_sublevel_set()