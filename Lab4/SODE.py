from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def function(eq, t, a, b, c):
    y1, y2, y3 = eq
    return [-y2 - y3, y1 + a * y2, b + y3 * (y1 - c)]
def task():
    a = 0.2
    b = 0.2
    c = 5.0

    y0 = [1.0, 1.0, 1.0]

    # Time points
    t = np.arange(0, 100, 0.1)

    # Solve the system of ODEs
    solution = odeint(function, y0, t, args=(a, b, c))
    print(solution)

    # Визуализация решения
    plt.figure(figsize=(12, 8))

    # Фазовый портрет y от x
    plt.subplot(2, 2, 1)
    plt.plot(solution[:, 0], solution[:, 1])
    plt.title('Фазовый портрет y от x')
    plt.xlabel('x')
    plt.ylabel('y')

    # График x от t
    plt.subplot(2, 2, 2)
    plt.plot(t, solution[:, 0])
    plt.title('График x от t')
    plt.xlabel('t')
    plt.ylabel('x')

    # График y от t
    plt.subplot(2, 2, 3)
    plt.plot(t, solution[:, 1])
    plt.title('График y от t')
    plt.xlabel('t')
    plt.ylabel('y')

    # График z от t
    plt.subplot(2, 2, 4)
    plt.plot(t, solution[:, 2])
    plt.title('График z от t')
    plt.xlabel('t')
    plt.ylabel('z')

    plt.tight_layout()
    plt.show()