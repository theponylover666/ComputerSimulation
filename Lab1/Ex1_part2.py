from cvxopt import matrix, solvers
import time

start = time.time()  # Начало отсчета времени выполнения программы

c = matrix([-120.0, -50.0, -30.0, -100.0])  # Коэффициенты целевой функции (отрицательные для максимизации)
G = matrix([[18.0, 150.0, 170.0, 31.0, -200.0],   # Матрица коэффициентов для неравенств G*x <= h
            [26.0, 140.0, 230.0, 42.0, -150.0],
            [16.0, 50.0, 280.0, 30.0, -170.0],
            [10.0, 80.0, 120.0, 20.0, -50.0]])
h = matrix([110000.0, 950000.0, 1200000.0, 180000.0, -750000.0])  # Вектор правых частей неравенств G*x <= h
A = None  # Матрица A для равенств A*x = b (отсутствует в данной задаче)
b = None  # Вектор b для равенств A*x = b (отсутствует в данной задаче)

# Ограничения на значения переменных
G_bounds = matrix([[-1.0, 0.0, 0.0, 0.0],  # x1 >= 1200
                   [0.0, -1.0, 0.0, 0.0],  # x2 >= 1000
                   [0.0, 0.0, -1.0, 0.0],  # x3 >= 1500
                   [0.0, 0.0, 0.0, -1.0]]) # x4 >= 1200
h_bounds = matrix([-1200.0, -1000.0, -1500.0, -1200.0])  # Правые части неравенств для ограничений на переменные

# Объединение ограничений и границ переменных
G = matrix([G, G_bounds])
h = matrix([h, h_bounds])

# Отключение вывода процесса решения
solvers.options['show_progress'] = False
# Решение задачи линейного программирования
solution = solvers.lp(c, G, h, A, b)

print("Результат:")
for i, val in enumerate(solution['x']):
    print(f"x{i+1} = {val}")  # Вывод результата для каждой переменной

print("Прибыль:")
print(-solution['primal objective'])  # Вывод значения целевой функции (смена знака, т.к. была минимизация)

stop = time.time()  # Конец отсчета времени
print("Время :")
print(stop - start)  # Вывод времени выполнения программы