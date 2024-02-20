import numpy as np
import time
from matplotlib import pyplot as plt
from Lab2.GenFibonacci import statistical_test, frequency_test

def generate_clipped_noncentral_f_numbers(dfnum, dfden, nc, size=1):
    """
    Генерация случайных чисел из нецентрального F-распределения и ограничение их диапазоном [0, 1].

    Параметры:
    - dfnum: степени свободы числителя (degrees of freedom of the numerator).
    - dfden: степени свободы знаменателя (degrees of freedom of the denominator).
    - nc: параметр нецентральности (noncentrality parameter).
    - size: размер выводимой выборки.

    Возвращает:
    - Массив случайных чисел из нецентрального F-распределения, ограниченный диапазоном [0, 1].
    """
    # Инициализируем массив для результатов
    random_numbers = np.empty(size)
    # Маска для выбора недопустимых значений
    mask = np.ones(size, dtype=bool)
    while np.any(mask):
        # Генерация значений для всех недопустимых позиций
        random_sample = np.random.noncentral_f(dfnum, dfden, nc, np.sum(mask))
        # Обновление недопустимых значений в массиве результатов
        random_numbers[mask] = random_sample
        # Обновление маски для исключения 0 и 1
        mask = (random_numbers <= 0) | (random_numbers >= 1)
    return random_numbers

dfnum = 5  # Степени свободы числителя
dfden = 10  # Степени свободы знаменателя
nc = 2  # Параметр нецентральности

# Запрашиваем у пользователя количество генерируемых чисел
size = int(input("Введите количество сгенерированных чисел: \n"))

# Начало отсчета времени выполнения программы
start = time.time()

clipped_random_numbers = generate_clipped_noncentral_f_numbers(dfnum, dfden, nc, size)

# Конец отсчета времени
stop = time.time()
print("Время :\n" + str(stop - start))

print(clipped_random_numbers)

# Применение тестов к сгенерированной последовательности
mean, variance, mean_condition, variance_condition = statistical_test(clipped_random_numbers)
frequency_percentage, frequency_condition, balance_condition = frequency_test(clipped_random_numbers)

# Вывод результатов
print(f"Математическое ожидание: {mean}, условие выполнено: {mean_condition}")
print(f"Дисперсия: {variance}, условие выполнено: {variance_condition}")
print(f"Процент чисел в интервале (0.2113; 0.7887): {frequency_percentage}%, условие выполнено: {frequency_condition}")
print(f"Баланс чисел в интервалах (0; 0.5) и (0.5; 1) сохранен: {balance_condition}")

# Гистограмма распределения сгенерированных чисел
plt.hist(clipped_random_numbers, bins=50, color='blue', alpha=0.7)
plt.title('Гистограмма распределения сгенерированных чисел')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()