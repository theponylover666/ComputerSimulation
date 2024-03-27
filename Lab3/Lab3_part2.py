import random
import simpy
import Multi_channel

def part2():
    def read_input_data(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            data = [line.split('#')[0].strip() for line in lines]  # Удаление комментариев и лишних пробелов
        return data

    # Загрузка данных из файла
    input_data = read_input_data('input_data.txt')

    # Допустимые входные параметры
    NUM_ATMS = int(input_data[0])  # Количество банкоматов, которые могут обслуживаться одновременно
    MAX_CLIENTS = int(input_data[1])  # Максимальное количество клиентов в системе
    LAMBDA = float(input_data[2])  # Среднее количество клиентов, прибывающих за минуту
    SIM_TIME = int(input_data[3])  # Общее время моделирования

    # Параметры треугольного распределения для времени обслуживания
    MIN_SERVICE_TIME = float(input_data[4])  # минимальное время
    MODE_SERVICE_TIME = float(input_data[5])  # наиболее вероятное время
    MAX_SERVICE_TIME = float(input_data[6])  # максимальное время

    class BankOffice(object):
        def __init__(self, env, num_atms):
            self.env = env
            self.atm = simpy.Resource(env, num_atms)
            self.allClients = 0
            self.accomplishedClients = 0

        def serve_client(self, client):
            """Процесс обслуживания клиента с треугольным временем"""
            service_time = random.triangular(MIN_SERVICE_TIME, MAX_SERVICE_TIME, MODE_SERVICE_TIME)
            yield self.env.timeout(service_time)
            self.allClients += 1
            print(f"{client} обслужен за {service_time:.2f} мин. в {self.env.now:.2f}")
            writefile('atm.txt', f"{client} обслужен за {service_time:.2f} мин. в {self.env.now:.2f}")
            if self.allClients % 5 == 0:  # Показать статистику каждого 5-го клиента
                print(f"Всего обслужено клиентов: {self.allClients}")
                writefile('atm.txt', f"Всего обслужено клиентов: {self.allClients}")

    def client(env, name, bank_office, max_queue_length):
        """Клиент приходит и обслуживается в банковском офисе"""
        if len(bank_office.atm.queue) < max_queue_length:
            with bank_office.atm.request() as request:
                yield request
                print(f"{name} начинает обслуживание в {env.now:.2f}")
                writefile('atm.txt', f"{name} начинает обслуживание в {env.now:.2f}")
                yield env.process(bank_office.serve_client(name))
                print(f"{name} покидает банк в {env.now:.2f}")
                writefile('atm.txt', f"{name} покидает банк в {env.now:.2f}")
        else:
            # Отказ в обслуживании из-за переполненной очереди
            print(f"{name} получает отказ из-за полной очереди в {env.now:.2f}")
            writefile('atm.txt', f"{name} получает отказ из-за полной очереди в {env.now:.2f}")

    def setup(env, num_atms, lambda_):
        """Создать банковский офис и генерировать клиентов"""
        bank_office = BankOffice(env, num_atms)

        # Генерировать новых клиентов
        i = 0
        while True:
            yield env.timeout(random.expovariate(lambda_))
            i += 1
            env.process(client(env, f'Клиент_{i}', bank_office, MAX_CLIENTS - NUM_ATMS))

    def writefile(file_path, text):
        # Записываем сообщения в файл
        with open(file_path, 'a') as file:
            file.write(text + '\n')

    def clear_file(file_path):
        """Очистка содержимого файла."""
        open(file_path, 'w').close()

    # Инициализировать и запустить симуляцию
    print("Начало симуляции")
    clear_file('atm.txt')
    random.seed()  # Инициализация генератора случайных чисел
    env = simpy.Environment()
    env.process(setup(env, NUM_ATMS, LAMBDA))
    env.run(until=SIM_TIME)

    #Подсчёт характеристик СМО
    mu = 1 / ((MIN_SERVICE_TIME + MODE_SERVICE_TIME + MAX_SERVICE_TIME) / 3)
    results = Multi_channel.With_Limited_Queue(NUM_ATMS, MAX_CLIENTS - NUM_ATMS, LAMBDA, mu)
    print("Характеристики СМО: \n" + results)
    writefile('atm.txt', "Характеристики СМО: \n" + results)

def part1():
    def generate_clients(env, lambda_, service_station, serviced_clients, denied_services):
        """Генерация клиентов с заданной интенсивностью lambda_."""
        while True:
            yield env.timeout(random.expovariate(lambda_))
            c = client(env, service_station, serviced_clients, denied_services)
            env.process(c)

    def client(env, service_station, serviced_clients, denied_services):
        """Попытка обслуживания клиента."""
        with service_station.request() as request:
            result = yield request | env.timeout(0)  # Попытка получить доступ к линии сразу
            if request in result:
                serviced_clients[0] += 1
                yield env.timeout(1)  # Время обслуживания
            else:
                denied_services[0] += 1

    def execute():
        # Параметры системы
        lambda_ = 0.95
        T_obs = 1
        SIM_TIME = 100

        serviced_clients = [0]  # использование списка для изменяемости в функции
        denied_services = [0]

        env = simpy.Environment()
        service_station = simpy.Resource(env, capacity=1)

        # Частичное применение функции для передачи дополнительных параметров
        env.process(generate_clients(env, lambda_, service_station, serviced_clients, denied_services))
        env.run(until=SIM_TIME)

        # Расчет результатов
        P_obs = serviced_clients[0] / (serviced_clients[0] + denied_services[0])
        P_otk = denied_services[0] / (serviced_clients[0] + denied_services[0])
        N_obs = serviced_clients[0] / SIM_TIME
        N_otk = denied_services[0] / SIM_TIME
        ratio = N_obs / N_otk if N_otk > 0 else float('inf')

        # Вывод результатов
        print(f"Вероятность обслуживания: {P_obs:.2f}")
        print(f"Вероятность отказа: {P_otk:.2f}")
        print(f"Число обслужанных заявок: {N_obs:.2f}")
        print(f"Число необслужанных заявок: {N_otk:.2f}")
        print(f"Отношение обслужанных к необслуженным заявкам: {ratio:.2f}")

    # Вызов функции для запуска симуляции
    execute()

def safe_input(prompt, expected_type):
    while True:
        try:
            return expected_type(input(prompt).replace(',', '.'))
        except ValueError:
            print(f"Ошибка: пожалуйста, введите значение типа {expected_type.__name__}")

choose = 1
while(choose > 0):
    print("\033[1mВыберите, что хотите выполнить\033[0m\n" +  "1.Задачу из второй части 3 лабораторной\n" + "2.Задачу из первой части 3 лабораторной(на SimPy, задача с одноканальной СМО с отказами в обслуживании)\n" + "0.Выход")
    choose = safe_input("", int)
    print("\n" * 5)
    match choose:
        case 1:
            part2()
        case 2:
            part1()
        case 0:
            break
        case _:
            print("Такого варианта нет")