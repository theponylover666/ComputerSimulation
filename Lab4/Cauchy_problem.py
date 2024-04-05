from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def func1(y, t):
    return y**2 - y*t

def func2(y, t):
    return y**2 + 1

def task():
    y0 = 0.0

    ti = np.arange(0, 1.1, 0.1)

    solution1 = odeint(func1, y0, ti)
    solution2 = odeint(func2, y0, ti)

    print(solution1)
    print(solution2)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(ti, solution1, 'r', label='y\' = y^2 - yt')
    plt.title('Решение of y\' = y^2 - yt')
    plt.xlabel('Время')
    plt.ylabel('y(t)')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(ti, solution2, 'b', label='y\' = y^2 + 1')
    plt.title('Решение of y\' = y^2 + 1')
    plt.xlabel('Время')
    plt.ylabel('y(t)')
    plt.legend()

    plt.tight_layout()
    plt.show()
