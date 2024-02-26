def With_Denial_Of_Service(lambda_, T_obs):
    # Параметры системы
    """
    lambda_ = 0.95
    T_obs = 1
    """
    mu = 1 / T_obs  # интенсивность обслуживания, вызовы в минуту

    # Расчёт вероятности обслуживания
    P_obs = mu / (lambda_ + mu)

    # Расчёт вероятности отказа
    P_otk = lambda_ / (lambda_ + mu)

    # Число обслужанных заявок в минуту
    N_obs = (lambda_ * mu) / (lambda_ + mu)

    # Число необслужанных заявок в минуту
    N_otk = (lambda_ * P_otk)

    # Отношение числа обслуженных к числу необслуженных заявок
    ratio = N_obs / N_otk

    result = ""

    result += ("Вероятность обслуживания: " + str(P_obs) + "\n")
    result += ("Вероятность отказа: " + str(P_otk) + "\n")
    result += ("Число обслужанных заявок: " + str(N_obs) + "\n")
    result += ("Число необслужанных заявок: " + str(N_otk) + "\n")
    result += ("Отношение обслужанных к необслужанным заявкам: " + str(ratio) + "\n")
    return result

def With_Limited_Queue(m, lambda_, mu):
    # Параметры системы
    """
    m = 3
    lambda_ = 0.7  # интенсивность потока заявок, вызовы в минуту
    mu = 1.25  # интенсивность обслуживания, вызовы в минуту
    """
    ro = lambda_ / mu

    #P0
    if ro == 1:
        P_0 = 1 / (m + 2)
    else:
        P_0 = (1 - ro) / (1 - ro ** (m + 2))

    # Расчёт вероятности отказа
    P_otk = P_0 * (ro ** (m + 1))

    # Расчёт вероятности обслуживания
    P_obs = lambda_ / (lambda_ + mu)

    # Относительная пропускная способность
    Q = 1 - P_otk

    # Абсолютная пропускная способность
    A = lambda_ * Q

    # Средняя длина очереди
    if ro == 1:
        L_queue = (m * (m + 1)) / (2 * (m + 2))
    else:
        L_queue = (ro ** 2) * ((1 - ro ** m * (m - m * ro + 1)) / ((1 - ro) ** 2))

    # Среднее время ожидания в очереди
    T_queue = L_queue / lambda_

    # Среднее число заявок в СМО
    L_SMO = 1 + L_queue

    # Среднее время нахождения заявки в СМО
    if ro == 1:
        T_SMO = (m + 1) / (2 * mu)
    else:
        T_SMO = L_SMO / lambda_

    result = ""

    result += ("P_0: "  + str(P_0) + "\n")
    result += ("Вероятность обслуживания: " + str(P_obs) + "\n")
    result += ("Вероятность отказа: " + str(P_otk) + "\n")
    result += ("Средняя длина очереди: " + str(L_queue) + "\n")
    result += ("Среднее время ожидания в очереди: " + str(T_queue) + "\n")
    result += ("Относительная пропускная способность: " + str(Q) + "\n")
    result += ("Абсолютная пропускная способность: " + str(A) + "\n")
    result += ("Среднее число заявок в СМО: " + str(L_SMO) + "\n")
    result += ("Cреднее время нахождения заявки в СМО: " + str(T_SMO) + "\n")
    return result

def With_Unlimited_Queue(lambda_, T_obs):
    # Параметры системы
    """
    lambda_ = 0.8
    T_obs = 1
    """

    mu = 1 / T_obs
    ro = lambda_ / mu
    result = ""

    #P0
    if ro >= 1:
        result += "Стационарное состояние невозможно"
        return result
    else:
        L_queue = (ro ** 2) / (1 - ro)
        T_queue = L_queue / lambda_
        L_SMO = ro / (1 - ro)
        T_SMO = L_SMO / lambda_

    result += ("Среднее число заявок в очереди: " + str(round(L_queue,2)) + "\n")
    result += ("Среднее время ожидания в очереди: " + str(round(T_queue,2)) + "\n")
    result += ("Среднее число заявок в СМО: " + str(round(L_SMO,2)) + "\n")
    result += ("Среднее время нахождения заявки в СМО: " + str(round(T_SMO,2)) + "\n")
    return result