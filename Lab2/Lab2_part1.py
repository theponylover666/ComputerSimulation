from scipy import fft
from numpy import arange, cos, pi
from matplotlib import pyplot as plt

# Задание параметров для сигнала
A = 2  # Амплитуда
fi: float = pi/8  # Фазовый сдвиг
T = 150  # Период
N = arange(1024)  # Массив временных точек от 0 до 1023

# Генерация сигнала с использованием заданных параметров
Xk = A * cos((2 * pi * N / T) + fi)
print(Xk)  # Вывод функции сигнала

# Вычисление прямого преобразования Фурье для сигнала
DFT = fft.fft(Xk)
print(DFT)  # Вывод прямого преобразования Фурье

# Вычисление обратного преобразования Фурье
IFT = fft.ifft(DFT)
print(IFT)  # Вывод обратного преобразования Фурье

# Создание рисунка с тремя областями для графиков
fig, axs = plt.subplots(3, 1, figsize=(14, 10))

# График исходного сигнала
axs[0].plot(Xk, 'b')
axs[0].set_title('Исходный сигнал')
axs[0].set_ylabel('Амплитуда')

# График модуля прямого преобразования Фурье
axs[1].plot(abs(DFT), 'r')
axs[1].set_title('Прямое преобразование Фурье (модуль)')
axs[1].set_ylabel('Амплитуда')

# График обратного преобразования Фурье
# Здесь стоит использовать abs(IFT) чтобы избежать ComplexWarning
axs[2].plot(IFT, 'g')
axs[2].set_title('Обратное преобразование Фурье (модуль)')
axs[2].set_ylabel('Амплитуда')
axs[2].set_xlabel('k')

# Подгонка и отображение графиков
plt.tight_layout()
plt.show()