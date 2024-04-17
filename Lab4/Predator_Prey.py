from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def func1(state, t, r1, alpha1, alpha2, beta2):
    x, y = state
    return [r1 * x - alpha1 * x * y, alpha2 * x * y - beta2 * y]

def func2(state, t, r1, alpha1, alpha2, beta2, g1):
    x, y = state
    return [r1 * x - alpha1 * x * y - g1 * x**2, alpha2 * x * y - beta2 * y]

def task():
    r1 = 0.5
    alpha1 = 0.01
    alpha2 = 0.01
    beta2 = 0.2
    g1 = 0.0005
    x0 = 25
    y0 = 5

    initial_state = [x0, y0]

    time = np.arange(0, 1000, 0.01)

    solution1 = odeint(func1, initial_state, time, args=(r1, alpha1, alpha2, beta2))
    print(solution1)

    x1, y1 = solution1.T

    solution2 = odeint(func2, initial_state, time, args=(r1, alpha1, alpha2, beta2, g1))
    print(solution1)

    x2, y2 = solution2.T

    plt.figure(figsize=(12, 10))

    plt.subplot(2, 2, 1)
    plt.plot(time, x1, label='Плотность "Жертвы" x(t)')
    plt.plot(time, y1, label='Плотность "Хищника" y(t)')
    plt.title('Плотность с течением времени')
    plt.xlabel('Время')
    plt.ylabel('Плотность')
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(x1, y1)
    plt.title('Фазовый портрет без конкуренции')
    plt.xlabel('Плотность "Жертвы" x')
    plt.ylabel('Плотность "Хищника" y')

    plt.subplot(2, 2, 3)
    plt.plot(time, x2, label='Плотность "Жертвы" x(t) с конкуренцией')
    plt.plot(time, y2, label='Плотность "Хищника" y(t) с конкуренцией')
    plt.title('Плотность с течением времени с конкуренцией')
    plt.xlabel('Время')
    plt.ylabel('Плотность')
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(x2, y2)
    plt.title('Фазовый портрет с конкуренцией')
    plt.xlabel('Плотность "Жертвы" x с конкуренцией')
    plt.ylabel('Плотность "Хищника" y с конкуренцией')

    plt.tight_layout()
    plt.show()