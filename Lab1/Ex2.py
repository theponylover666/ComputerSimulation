# Полностью автоматическое создание трендов с matplotlib
import matplotlib.pyplot as plt # импортируем построитель графиков из библиотеки matplotlib
import numpy as np # импортируем библиотеку numpy для работы с массивами numpy
from sklearn.metrics import r2_score # функция для расчёта критерия r^2
import matplotlib.dates as mdates
from datetime import datetime

# Массив дат (оси x)
date_strings = ['2023-3-15', '2023-3-14', '2023-3-13', '2023-3-10', '2023-3-9', '2023-3-8',
        '2023-3-7', '2023-3-6', '2023-3-3', '2023-3-2', '2023-3-1', '2023-2-28',
        '2023-2-27', '2023-2-24', '2023-2-23', '2023-2-22', '2023-2-21',
        '2023-2-20', '2023-2-17', '2023-2-16', '2023-2-15']

# Преобразование списка строк дат в массив объектов datetime
dates = [datetime.strptime(date, '%Y-%m-%d') for date in date_strings]
x = mdates.date2num(dates)

# Массив значений (оси y)
y = [132.99, 134.22, 133.18, 134.98, 136.14, 137.34, 137.14, 135.91, 135.86, 136.76, 136.16,
            136.2, 136.2, 136.46, 134.7, 134.9, 134.99, 134.23, 134.15, 133.94, 134.11]

# Линии тренда
# линейный (автоматическое создание)
set_line_by_data = np.polyfit(x, y, 1) # полином первой степени
linear_trend = np.poly1d(set_line_by_data) # снижение размерности до одномерного массива
print("{0}x + {1}".format(*set_line_by_data)) # формула

# полиномиальный
set_polinom_by_data = np.polyfit(x, y, 6) # работа с полиномом 6 степени
polinom_trend = np.poly1d(set_polinom_by_data) # Рассчитать значение полинома в точках x
print("${0}x^6 + {1}x^5 + {2}x^4 + {3}x^3 + {4}x^2 + {5}x + {6}$".format(*set_polinom_by_data)) # формула

# логарифмический
set_log_by_data = np.polyfit(np.log(x), y, 1) # работа с полиномом 1 степени + логарифмирование x
log_trend = [set_log_by_data[0]*np.log(x) + set_log_by_data[1] for x in x] # создание одномерного массива для логарифмического тренда
print("${0}ln(x) + {1}$".format(*set_log_by_data))  # формула

# экспоненциальный
set_exp_by_data = np.polyfit(x, np.log(y), 1) # работа с полиномом 1 степени + логарифмирование
exp_trend = [np.exp(set_exp_by_data[1]) * np.exp(set_exp_by_data[0] * x) for x in x] # создание одномерного массива для экспоненциального тренда
print("${1}e^{0}x$".format(*set_exp_by_data))  # формула

# Расчёт R^2
linear_r2 = r2_score(y, linear_trend(x))
polinom_r2 = r2_score(y, polinom_trend(x))
log_r2 = r2_score(y, log_trend)
exp_r2 = r2_score(y, exp_trend)

# Отображение графика
plt.figure(figsize=(15, 15))

# 2 графика по горизонтали, 2 по вертикали
plt.subplot(2, 2, 1)
plt.scatter(dates, y, label='data')
plt.plot(dates, linear_trend(x), linestyle='dashed', color="orange", label='linear trend')
plt.grid(color="gainsboro")
plt.legend(loc='upper right', fontsize=12)
plt.title("Линейный \n$R^2=$" + str(linear_r2) + "\n{0}x + {1}".format(*set_line_by_data))

# 2 графика по горизонтали, 2 по вертикали
plt.subplot(2, 2, 2)
plt.scatter(dates, y, label='data')
x = np.linspace(x.min(), x.max(), 100)  # Создаем больше точек для плавной кривой
plt.plot(x, polinom_trend(x), linestyle='dashed', color="orange", label='polinomial trend')
plt.grid(color="gainsboro")
plt.legend(loc='center left', fontsize=12, bbox_to_anchor=(1, 0.5))
plt.title("Полиномиальный \n$R^2=$" + str(polinom_r2) + "\n${0}x^6 + {1}x^5$ + \n${2}x^4 + {3}x^3$ + \n${4}x^2 + {5}x$ + \n${6}$".format(*set_polinom_by_data))

# 2 графика по горизонтали, 2 по вертикали
plt.subplot(2, 2, 3)
plt.scatter(dates, y, label='data')
plt.plot(dates, log_trend, linestyle='dashed', color="orange", label='log trend')
plt.grid(color="gainsboro")
plt.legend(loc='upper right', fontsize=12)
plt.title("Логарифмический \n$R^2=$" + str(log_r2) + "\n${0}ln(x) + {1}$".format(*set_log_by_data))

# 2 графика по горизонтали, 2 по вертикали
plt.subplot(2, 2, 4)
plt.scatter(dates, y, label='data')
plt.plot(dates, exp_trend, linestyle='dashed', color="orange", label='exp trend')
plt.grid(color="gainsboro")
plt.legend(loc='center left', fontsize=12, bbox_to_anchor=(1, 0.5))
plt.title("Экспоненциальный \n$R^2=$" + str(exp_r2) + "\n{1}e^({0}x)".format(*set_exp_by_data))

fig = plt.gcf()
fig.set_size_inches(10, 10)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Формат дат на оси X
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))  # Интервал между метками

plt.xticks(rotation=45)  # Повернуть метки дат для лучшей читаемости

plt.tight_layout()  # Улучшить компоновку графиков

plt.show()


