from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def predator_prey_system(state, t, r1, alpha1, alpha2, beta2, g1):
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

    time = np.arange(0, 1000, 10)

    solution = odeint(predator_prey_system, initial_state, time, args=(r1, alpha1, alpha2, beta2, g1))

    x, y = solution.T

    plt.figure(figsize=(12, 10))

    plt.subplot(2, 2, 1)
    plt.plot(time, x, label='Плотность "Жертвы" x(t)')
    plt.plot(time, y, label='Плотность "Хищника" y(t)')
    plt.title('Плотность населения с течением времени')
    plt.xlabel('Время')
    plt.ylabel('Плотность')
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(x, y)
    plt.title('Фазовый портрет без конкуренции')
    plt.xlabel('Плотность "Жертвы" x')
    plt.ylabel('Плотность "Хищника" y')

    plt.subplot(2, 2, 3)
    plt.plot(time, x, label='Плотность "Жертвы" x(t) с конкуренцией')
    plt.plot(time, y, label='Плотность "Хищника" y(t) с конкуренцией')
    plt.title('Плотность населения с течением времени с конкуренцией')
    plt.xlabel('Время')
    plt.ylabel('Плотность')
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(x, y)
    plt.title('Фазовый портрет с конкуренцией')
    plt.xlabel('Плотность "Жертвы" x с конкуренцией')
    plt.ylabel('Плотность "Хищника" y с конкуренцией')

    plt.tight_layout()
    plt.show()