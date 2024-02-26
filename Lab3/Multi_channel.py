from scipy.special import factorial
import numpy as np

def With_Denial_Of_Service(n, lambda_, mu):
    # Параметры системы
    """
    n = 3  # количество каналов обслуживания
    lambda_ = 3  # интенсивность входящего потока
    mu = 2  # интенсивность обслуживания одним каналом
    """

    # Расчет загрузки системы
    ro = lambda_ / mu

    # Интенсивность обслуживания заявок (P0)
    sum_rho = sum([(ro ** k) / factorial(k) for k in range(n)])
    P_0 = (sum_rho) ** -1

    # Вероятность отказа (Pотк)
    P_otk = P_0 * ((ro ** n) / factorial(n))

    # Вероятность обслуживания (Pобсл)
    P_obsl = 1 - P_otk

    # Относительная пропускная способность (Q)
    Q = P_obsl

    # Абсолютная пропускная способность (A)
    A = lambda_ * Q

    # Среднее число занятых каналов (k)
    k_average = A / mu

    result = ""

    result += ("Интенсивность потока заявок: " + str(ro) + "\n")
    result += ("Интенсивность обслуживания заявок: " + str(P_0) + "\n")
    result += ("Вероятность отказа: " + str(P_otk) + "\n")
    result += ("Вероятность обслуживания: " + str(P_obsl) + "\n")
    result += ("Относительная пропускная способность: " + str(Q) + "\n")
    result += ("Абсолютная пропускная способность: " + str(A) + "\n")
    result += ("Среднее число занятых каналов: " + str(k_average) + "\n")
    return result

def With_Limited_Queue(n, m, lambda_, mu):
    # Параметры системы
    """
    n = 3  # количество каналов обслуживания
    m = 5 # длина очереди
    lambda_ = 3  # интенсивность входящего потока
    mu = 2  # интенсивность обслуживания одним каналом
    """

    # Расчет загрузки системы
    ro = lambda_ / mu
    ro_n = ro / n

    sum_rho = sum([ ((ro ** k) / factorial(k)) for k in range(n + 1)])

    # Вероятность нулевой очереди (P0)
    if ro_n == 1:
        P_0 = (sum_rho + ((m * (ro ** (n+1)))/(n * factorial(n)))) ** -1
    else:
        P_0 = (sum_rho + ((((ro ** (n + 1))) / (factorial(n) * (n - ro))) * (1 - ((ro/n) ** m)))) ** -1

    # Вероятность отказа (Pотк)
    P_otk = ((ro ** (n + m)) / ((n ** m) * (factorial(n)))) * P_0

    helper = (ro ** (n + 1)) / (n * factorial(n))
    # Средняя длина очереди (Lоч)
    if ro_n == 1:
        L_queue = (helper * ((m * (m + 1))/(2))) * P_0
    else:
        L_queue = (helper * ((1 - (ro_n ** m) * (m + 1 - m * ro_n))/((1-ro_n) ** 2)))

    # Среднее время ожидания в очереди (Tоч)
    T_queue = L_queue / lambda_

    # Среднее время нахождения заявки в СМО (Lсмо)
    T_SMO = T_queue + ((1 - P_otk) / mu)

    # Среднее время пребывания заявки в системе (Tсмо)
    k_average = (lambda_ / mu) * (1 - P_otk)

    result = ""

    result += ("Вероятность нулевой очереди: " + str(P_0) + "\n")
    result += ("Вероятность отказа: " + str(P_otk) + "\n")
    result += ("Средняя длина очереди: " + str(L_queue) + "\n")
    result += ("Среднее время ожидания в очереди: " + str(T_queue) + "\n")
    result += ("Среднее время нахождения заявки в СМО: " + str(T_SMO) + "\n")
    result += ("Среднее число занятых каналов: " + str(k_average) + "\n")
    return result

def With_Unlimited_Queue(n, lambda_, mu):
    # Параметры системы
    """
    n = 3  # количество каналов обслуживания
    lambda_ = 3  # интенсивность входящего потока
    mu = 2  # интенсивность обслуживания одним каналом
    """

    # Расчет загрузки системы
    ro = lambda_ / (n * mu)

    # Проверка на устойчивость системы
    if ro >= 1:
        raise ValueError("Система нестабильна, так как ro >= 1")

    # Вероятность нулевой очереди (P0)
    sum_rho = sum([(n * ro) ** k / factorial(k) for k in range(n)])
    P_0 = (sum_rho + (n * ro) ** n / (factorial(n) * (1 - ro))) ** -1

    # Вероятность образования очереди (Pоч)
    P_queue = (n * ro) ** (n + 1) / (factorial(n) * (n - (ro * n))) * P_0

    # Средняя длина очереди (Lоч)
    L_queue = (n * ro) ** n * ro / (factorial(n) * (1 - ro) ** 2) * P_0

    # Среднее время ожидания в очереди (Tоч)
    T_queue = L_queue / lambda_

    # Среднее число заявок в системе (Lсмо)
    L_SMO = L_queue + n * ro

    # Среднее время пребывания заявки в системе (Tсмо)
    T_SMO = T_queue + 1 / mu

    result = ""

    result += ("Вероятность нулевой очереди: " + str(P_0) + "\n")
    result += ("Вероятность образования очереди: " + str(P_queue) + "\n")
    result += ("Средняя длина очереди: " + str(L_queue) + "\n")
    result += ("Среднее время ожидания в очереди: " + str(T_queue) + "\n")
    result += ("Среднее число заявок в СМО: " + str(L_SMO) + "\n")
    result += ("Среднее время нахождения заявки в системе: " + str(T_SMO) + "\n")
    return result