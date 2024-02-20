import matplotlib.pyplot as plt
import time
from Lab2.GenFibonacci import FibonacciGenerator, statistical_test, frequency_test

# Запрашиваем у пользователя количество генерируемых чисел
n = int(input("Введите количество сгенерированных чисел: \n"))

# Начало отсчета времени выполнения программы
start = time.time()

# Выполнение генерации чисел
randomizer = FibonacciGenerator(n)

# Конец отсчета времени
stop = time.time()
print("Время :\n" + str(stop - start))

# Выводим сгенерированные числа
if(randomizer.size < 15):
    print(randomizer)

# Применение тестов к сгенерированной последовательности
mean, variance, mean_condition, variance_condition = statistical_test(randomizer)
frequency_percentage, frequency_condition, balance_condition = frequency_test(randomizer)

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

# Гистограмма распределения сгенерированных чисел
plt.hist(randomizer, bins=50, color='blue', alpha=0.7)
plt.title('Гистограмма распределения сгенерированных чисел')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()