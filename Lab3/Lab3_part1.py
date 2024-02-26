from Lab3 import Single_channel, Multi_channel

def safe_input(prompt, expected_type):
    while True:
        try:
            return expected_type(input(prompt).replace(',', '.'))
        except ValueError:
            print(f"Ошибка: пожалуйста, введите значение типа {expected_type.__name__}")

def SCWDOS():
    print("\033[1mОДНОКАНАЛЬНЫЕ СМО С ОТКАЗАМИ В ОБСЛУЖИВАНИИ\033[0m")
    print("Введите необходимые значение")
    lambda_ = safe_input("Интенсивность входящего потока: ", float)
    T_obs = safe_input("Средняя продолжительность разговора: ", float)
    print(Single_channel.With_Denial_Of_Service(lambda_, T_obs))

def SCWLQ():
    print("\033[1mОДНОКАНАЛЬНЫЕ СМО С ОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\033[0m")
    print("Введите необходимые значение")
    m = safe_input("Число мест в очереди: ", int)
    lambda_ = safe_input("Значение интенсивности клиентов: ", float)
    mu = safe_input("Интенсивность обслуживания одним каналом: ", float)
    print(Single_channel.With_Limited_Queue(m, lambda_, mu))

def SCWUQ():
    print("\033[1mОДНОКАНАЛЬНЫЕ СМО С НЕОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\033[0m")
    print("Введите необходимые значение")
    lambda_ = safe_input("Интенсивность входящего потока: ", float)
    T_obs = safe_input("Обслуживание одного рабочего: ", float)
    print(Single_channel.With_Unlimited_Queue(lambda_, T_obs))

def MCWDOS():
    print("\033[1m МНОГОКАНАЛЬНЫЕ СМО С ОТКАЗАМИ В ОБСЛУЖИВАНИИ\033[0m")
    print("Введите необходимые значение")
    n = safe_input("Количество каналов обслуживания: ", int)
    lambda_ = safe_input("Интенсивность входящего потока: ", float)
    mu = safe_input("Интенсивность обслуживания одним каналом: ", float)
    print(Multi_channel.With_Denial_Of_Service(n, lambda_, mu))

def MCWLQ():
    print("\033[1mМНОГОКАНАЛЬНЫЕ СМО С ОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\033[0m")
    print("Введите необходимые значение")
    n = safe_input("Количество каналов обслуживания: ", int)
    m = safe_input("Длина очереди: ", int)
    lambda_ = safe_input("Интенсивность входящего потока: ", float)
    mu = safe_input("Интенсивность обслуживания одним каналом: ", float)
    print(Multi_channel.With_Limited_Queue(n, m, lambda_, mu))

def MCWUQ():
    print("\033[1mМНОГОКАНАЛЬНЫЕ СМО С НЕОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\033[0m")
    print("Введите необходимые значение")
    n = safe_input("Количество каналов обслуживания: ", int)
    lambda_ = safe_input("Интенсивность входящего потока: ", float)
    mu = safe_input("Интенсивность обслуживания одним каналом: ", float)
    print(Multi_channel.With_Unlimited_Queue(n, lambda_, mu))

def TypicalTask():
    number = 1
    while (number > 0):
        print(
            "\033[1mВыберите задачу(напишите номер):\033[0m\n" + "1. Задача 1. ОДНОКАНАЛЬНЫЕ СМО С ОТКАЗАМИ В ОБСЛУЖИВАНИИ\n"
            + "2. Задача 2. ОДНОКАНАЛЬНЫЕ СМО С ОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\n" + "3. Задача 3. МНОГОКАНАЛЬНЫЕ СМО С НЕОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\n"
            + "4. Задача 4. ОДНОКАНАЛЬНЫЕ СМО С НЕОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\n" + "5. Задача 5. МНОГОКАНАЛЬНЫЕ СМО С НЕОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\n"
            + "6. Задача 6. МНОГОКАНАЛЬНЫЕ СМО С ОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\n" + "0. Выйти")
        number = safe_input("", int)
        print("\n" * 5)
        match number:
            case 1:
                print("\033[1mЗадача 1. ОДНОКАНАЛЬНЫЕ СМО С ОТКАЗАМИ В ОБСЛУЖИВАНИИ\033[0m")
                print(Single_channel.With_Denial_Of_Service(0.95, 1))
            case 2:
                print("\033[1mЗадача 2. ОДНОКАНАЛЬНЫЕ СМО С ОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\033[0m")
                print(Single_channel.With_Limited_Queue(3, 0.7, 1.25))
            case 3:
                print("\033[1mЗадача 3. МНОГОКАНАЛЬНЫЕ СМО С НЕОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\033[0m")
                print(Multi_channel.With_Unlimited_Queue(3, 0.8, 1))
            case 4:
                print("\033[1mЗадача 4. ОДНОКАНАЛЬНЫЕ СМО С ОТКАЗАМИ В ОБСЛУЖИВАНИИ\033[0m")
                print(Single_channel.With_Denial_Of_Service(0.5 * 60, 1.2 * 60))
            case 5:
                print("\033[1mЗадача 5. МНОГОКАНАЛЬНЫЕ СМО С НЕОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\033[0m")
                print(Multi_channel.With_Unlimited_Queue(3, 1, 3))
            case 6:
                print("\033[1mЗадача 6. МНОГОКАНАЛЬНЫЕ СМО С ОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\033[0m")
                print(Multi_channel.With_Limited_Queue(2, 5, 1 / 3, 1 / 2))
            case 0:
                break
            case _:
                print("Такого варианта нет...")

def PrivateTask():
    number = 1
    while (number > 0):
        print(
            "Выберите задачу(напишите номер):\n" + "1. ОДНОКАНАЛЬНЫЕ СМО С ОТКАЗАМИ В ОБСЛУЖИВАНИИ\n"
            + "2. ОДНОКАНАЛЬНЫЕ СМО С ОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\n" + "3. ОДНОКАНАЛЬНЫЕ СМО С НЕОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ "
            + "4. МНОГОКАНАЛЬНЫЕ СМО С ОТКАЗАМИ В ОБСЛУЖИВАНИИ\n" + "5. МНОГОКАНАЛЬНЫЕ СМО С ОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\n"
            + "6. МНОГОКАНАЛЬНЫЕ СМО С НЕОГРАНИЧЕННОЙ ОЧЕРЕДЬЮ\n" + "0. Выйти")
        number = safe_input("", int)
        print("\n" * 5)
        match number:
            case 1:
                SCWDOS()
            case 2:
                SCWLQ()
            case 3:
                SCWUQ()
            case 4:
                MCWDOS()
            case 4:
                MCWLQ()
            case 6:
                MCWUQ()
            case 0:
                break
            case _:
                print("Такого варианта нет...")

choose = 1
while(choose > 0):
    print("\033[1mВыберите, что хотите выполнить\033[0m\n" +  "1.Типовую задачу (готовые задачи)\n" + "2.Частный случай (ввести собственные данные)\n" + "0.Выход")
    choose = safe_input("", int)
    print("\n" * 5)
    match choose:
        case 1:
            TypicalTask()
        case 2:
            PrivateTask()
        case 0:
            break
        case _:
            print("Такого варианта нет")

