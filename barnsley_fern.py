import matplotlib.pyplot as plt
import random

def barnsley_fern(n=100000):
    x, y = 0.0, 0.0
    xs, ys = [], []

    for _ in range(n):
        xs.append(x)
        ys.append(y)
        r = random.random()

        if r < 0.01:
            x, y = 0.0, 0.16 * y
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x, y = 0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

    _, ax = plt.subplots(figsize=(6, 10))
    ax.scatter(xs, ys, s=0.1, c="green", marker=".")
    ax.set_title("Fougère de Barnsley")
    ax.set_aspect("equal")
    ax.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    barnsley_fern()
