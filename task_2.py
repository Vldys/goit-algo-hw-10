import scipy.integrate as spi
import random
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 2


def monte_carlo_integral(a, b, num_points):
    hits = 0
    max_y = 4

    for _ in range(num_points):
        x = random.uniform(a, b)
        y = random.uniform(0, max_y)

        if y <= f(x):
            hits += 1

    rectangle_area = (b - a) * max_y

    return rectangle_area * hits / num_points


a = 0
b = 2

result = monte_carlo_integral(a, b, 100000)

print("Метод Монте-Карло:", result)
print("Точное значение:", 8 / 3)
print("Абсолютная ошибка:", abs(result - 8 / 3))

quad_result, quad_error = spi.quad(f, a, b)

print("Результат quad:", quad_result)
print("Оценка ошибки quad:", quad_error)
print("Разница Монте-Карло и quad:", abs(result - quad_result))

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, "r", linewidth=2, label="f(x) = x²")

ix = np.linspace(a, b, 200)
iy = f(ix)

ax.fill_between(
    ix, iy,
    color="gray",
    alpha=0.3,
    label="Площа інтегрування"
)

ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")

ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Інтегрування f(x) = x² від 0 до 2")

ax.grid(True)
ax.legend()

plt.savefig("monte_carlo_integral.png", dpi=150, bbox_inches="tight")
plt.show()
