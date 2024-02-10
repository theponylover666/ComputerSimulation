import numpy
from numpy import *
import matplotlib.pyplot as plt
import time


# Задаем начальные значения для генератора Фибоначчи
Xi_0 = 3971
Xi_1 = 1013
k = 14
m = 2**k  # Вычисляем модуль m как 2 в степени k

# Запрашиваем у пользователя количество генерируемых чисел
n = int(input("Введите количество сгенерированных чисел: \n"))

start = time.time()  # Начало отсчета времени выполнения программы
# Создаем массив для хранения сгенерированных чисел
randomizer = empty(n, dtype=int64)
randomizer[0], randomizer[1] = Xi_0, Xi_1  # Инициализируем первые два числа

# Генерируем последовательность чисел методом Фибоначчи
for i in range(2, n):
    randomizer[i] = (randomizer[i - 1] + randomizer[i - 2]) % m

stop = time.time()  # Конец отсчета времени
print("Время :")
# Вывод времени выполнения программы
print(stop - start)
if(randomizer.size < 15):
    print(randomizer) # Выводим сгенерированные числа


plt.hist(randomizer, bins=50, color='blue', alpha=0.7)
plt.title('Гистограмма распределения сгенерированных чисел')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
# Подготовка функции для проверки статистических характеристик
def statistical_test(random_numbers, m):
    # Нормируем числа к интервалу [0, 1)
    normalized_numbers = random_numbers / m

    # Вычисление математического ожидания
    mean = numpy.mean(normalized_numbers)

    # Вычисление дисперсии
    variance = numpy.var(normalized_numbers)

    # Проверка условий равномерного распределения
    mean_condition = (mean > 0.5 - (1 / sqrt(12))) and (mean < 0.5 + (1 / sqrt(12)))
    variance_condition = (variance > (1 / 12) - (0.005)) and (variance < (1 / 12) + (0.005))

    return mean, variance, mean_condition, variance_condition

# Подготовка функции для частотного теста
def frequency_test(random_numbers, m):
    # Нормируем числа к интервалу [0, 1)
    normalized_numbers = random_numbers / m

    # Вычисление количества чисел в заданном интервале
    count_in_interval = numpy.sum((normalized_numbers > 0.2113) & (normalized_numbers < 0.7887))
    percentage_in_interval = (count_in_interval / len(random_numbers)) * 100

    # Проверка условий частотного теста
    frequency_condition = percentage_in_interval > (57.7 - 5) and percentage_in_interval < (57.7 + 5)

    # Проверка равенства количества чисел в интервалах (0; 0.5) и (0.5; 1)
    count_below_half = numpy.sum(normalized_numbers < 0.5)
    count_above_half = len(normalized_numbers) - count_below_half
    balance_condition = numpy.abs(count_below_half - count_above_half) < (0.1 * len(random_numbers))

    return percentage_in_interval, frequency_condition, balance_condition

# Применение тестов к сгенерированной последовательности
mean, variance, mean_condition, variance_condition = statistical_test(randomizer, m)
frequency_percentage, frequency_condition, balance_condition = frequency_test(randomizer, m)

# Вывод результатов
print(f"Математическое ожидание: {mean}, условие выполнено: {mean_condition}")
print(f"Дисперсия: {variance}, условие выполнено: {variance_condition}")
print(f"Процент чисел в интервале (0.2113; 0.7887): {frequency_percentage}%, условие выполнено: {frequency_condition}")
print(f"Баланс чисел в интервалах (0; 0.5) и (0.5; 1) сохранен: {balance_condition}")

# Записываем числа в файл
filename = "random_numbers.txt"  # Имя файла для сохранения
with open(filename, "w") as file:
    for number in randomizer:
        file.write(f"{number}\n")  # Записываем каждое число в отдельной строке

print(f"Числа были сохранены в файл {filename}.")