import numpy as np

def FibonacciGenerator(n):
    # Задаем начальные значения для генератора Фибоначчи
    Xi_0 = 3971
    Xi_1 = 1013
    k = 14
    m = 2**k  # Вычисляем модуль m как 2 в степени k

    array = np.empty(n, dtype=np.float64)  # Создаем массив для вещественных чисел
    array[0], array[1] = Xi_0, Xi_1  # Инициализируем первые два числа

    # Генерируем последовательность чисел методом Фибоначчи
    for i in range(2, n):
        array[i] = (array[i - 1] + array[i - 2]) % m

    # Нормализация чисел к диапазону [0, 1)
    array = array.astype(float) / m
    return array
# Подготовка функции для проверки статистических характеристик
def statistical_test(random_numbers):
    mean = np.mean(random_numbers)
    variance = np.var(random_numbers)

    # Условия для равномерного распределения
    mean_condition = (mean > 0.5 - (1 / np.sqrt(12))) and (mean < 0.5 + (1 / np.sqrt(12)))
    variance_condition = (variance > (1 / 12) - (0.005)) and (variance < (1 / 12) + (0.005))

    return mean, variance, mean_condition, variance_condition


def frequency_test(random_numbers):
    count_in_interval = np.sum((random_numbers > 0.2113) & (random_numbers < 0.7887))
    percentage_in_interval = (count_in_interval / len(random_numbers)) * 100

    # Условия для частотного теста
    frequency_condition = percentage_in_interval > (57.7 - 5) and percentage_in_interval < (57.7 + 5)

    count_below_half = np.sum(random_numbers < 0.5)
    count_above_half = len(random_numbers) - count_below_half
    balance_condition = np.abs(count_below_half - count_above_half) < (0.1 * len(random_numbers))

    return percentage_in_interval, frequency_condition, balance_condition