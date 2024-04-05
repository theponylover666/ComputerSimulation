from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def func1(y, t):
    y1, y2 = y
    return [y2, np.cos(t) - 2*y2 - 3*y1]

def func2(z, t, a):
    z1, z2 = z
    return [z2, a * (1 - z1**2) * z2 - z1]

def task():
    y0 = [0, 0]
    z0 = [2, 0]
    a = 1

    ti1 = np.arange(0, 2 * np.pi, 0.1)
    ti2 = np.arange(0, 30, 0.1)

    solution1 = odeint(func1, y0, ti1)
    solution2 = odeint(func2, z0, ti2, args=(a,))

    print(solution1)
    print(solution2)

    y1, y2 = solution1.T
    z1, z2 = solution2.T

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(ti1, y1, 'b')
    plt.plot(ti1, y2, 'g')
    plt.title('Решение y(t) и производная y\'(t) первого уравнения')
    plt.xlabel('Время t')
    plt.ylabel('y(t), y\'(t)')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(ti2, z1, 'b')
    plt.plot(ti2, z2, 'g')
    plt.title('Решение z(t) и производная z\'(t) первого уравнения')
    plt.xlabel('Время t')
    plt.ylabel('z(t), z\'(t)')
    plt.legend()

    plt.tight_layout()
    plt.show()