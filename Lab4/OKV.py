import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
def f(x):
    return (4 * (x ** 2) - x) # Замените на свою функцию

def integral(f, a, b, n, method):
    h=(b-a)/n
    x = np.arange(a, b, h)
    if method == 'left':
        return np.sum(f(x)*h), x, f(x)
    elif method == 'right':
        return np.sum(f(x+h)*h), x+h, f(x+h)
    elif method == 'center':
        return np.sum(f(x + h/2)*h), x + h/2, f(x + h/2)
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = h * (0.5*y[0] + 0.5*y[-1] + np.sum(y[1:-1]))
    return integral, x, y
def simpson_integral(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]))
    return integral, x, y
a = 0  # Начало интервала
b = 1  # Конец интервала
n1 = 10
n2 = 20
epsilon = 0.001  # Точность


left, x_left, y_left = integral(f, a, b, n1, 'left')
right, x_right, y_right = integral(f, a, b, n1, 'right')
center, x_center, y_center = integral(f, a, b, n1, 'center')
trapezoidal, x_trapezoidal, y_trapezoidal = trapezoidal_rule(a, b,n1)
simpson, x_simpson, y_simpson = simpson_integral(a, b, n1)


df_left = pd.DataFrame({'x': x_left, 'y': y_left})
df_right = pd.DataFrame({'x': x_right, 'y': y_right})
df_center = pd.DataFrame({'x': x_center, 'y': y_center})
df_trapezoidal = pd.DataFrame({'x': x_trapezoidal, 'y': y_trapezoidal})
df_simpson = pd.DataFrame({'x': x_simpson, 'y': y_simpson})

print(f'Левые прямоугольники: {left} при n={n1}\n', df_left)
print(f'Правые прямоугольники: {right} при n={n1}\n', df_right)
print(f'Центральные прямоугольники: {center} при n={n1}\n', df_center)
print(f"Метод трапеций: {trapezoidal} при n={n1}\n", df_trapezoidal)
print(f"Формула Симпсона: {simpson} при n={n1}\n", df_simpson)


left, x_left, y_left = integral(f, a, b, n2, 'left')
right, x_right, y_right = integral(f, a, b, n2, 'right')
center, x_center, y_center = integral(f, a, b, n2, 'center')
trapezoidal, x_trapezoidal, y_trapezoidal = trapezoidal_rule(a, b,n2)
simpson, x_simpson, y_simpson = simpson_integral(a, b, n2)


df_left = pd.DataFrame({'x': x_left, 'y': y_left})
df_right = pd.DataFrame({'x': x_right, 'y': y_right})
df_center = pd.DataFrame({'x': x_center, 'y': y_center})
df_trapezoidal = pd.DataFrame({'x': x_trapezoidal, 'y': y_trapezoidal})
df_simpson = pd.DataFrame({'x': x_simpson, 'y': y_simpson})

print(f'Левые прямоугольники: {left} при n={n2}\n', df_left)
print(f'Правые прямоугольники: {right} при n={n2}\n', df_right)
print(f'Центральные прямоугольники: {center} при n={n2}\n', df_center)
print(f"Метод трапеций: {trapezoidal} при n={n2}\n", df_trapezoidal)
print(f"Формула Симпсона: {simpson} при n={n2}\n", df_simpson)



left_n1, _, _ = integral(f, a, b, n1, 'left')
right_n1, _, _ = integral(f, a, b, n1, 'right')
center_n1, _, _ = integral(f, a, b, n1, 'center')
trapezoidal_n1, _, _ = trapezoidal_rule(a, b, n1)
simpson_n1, _, _ = simpson_integral(a, b, n1)

left_n2, _, _ = integral(f, a, b, n2, 'left')
right_n2, _, _ = integral(f, a, b, n2, 'right')
center_n2, _, _ = integral(f, a, b, n2, 'center')
trapezoidal_n2, _, _ = trapezoidal_rule(a, b, n2)
simpson_n2, _, _ = simpson_integral(a, b, n2)

df = pd.DataFrame({
    'Метод': ['Левые прямоугольники', 'Правые прямоугольники', 'Центральные прямоугольники', 'Метод трапеций', 'Формула Симпсона'],
    'Значение при n1': [left_n1, right_n1, center_n1, trapezoidal_n1, simpson_n1],
    'Значение при n2': [left_n2, right_n2, center_n2, trapezoidal_n2, simpson_n2],
    'разница': [abs(simpson_n2-left_n1), abs(simpson_n2-right_n1), abs(simpson_n2-center_n1), abs(simpson_n2-trapezoidal_n1), abs(simpson_n2-simpson_n1)],
    'Условие':[abs(simpson_n2-left_n1)<epsilon,abs(simpson_n2-right_n1)<epsilon,abs(simpson_n2-center_n1)<epsilon,abs(simpson_n2-trapezoidal_n1)<epsilon,abs(simpson_n2-simpson_n1)<epsilon],
    '': [abs(simpson_n2-left_n1)/simpson_n2*100, abs(simpson_n2-right_n1)/simpson_n2*100, abs(simpson_n2-center_n1)/simpson_n2*100, abs(simpson_n2-trapezoidal_n1)/simpson_n2*100, abs(simpson_n2-simpson_n1)/simpson_n2*100]
})

print(df)