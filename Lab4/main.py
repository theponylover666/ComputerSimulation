import Cauchy_problem, SODE, SO_equation, Predator_Prey, GUI

def safe_input(prompt, expected_type):
    while True:
        try:
            return expected_type(input(prompt).replace(',', '.'))
        except ValueError:
            print(f"Ошибка: пожалуйста, введите значение типа {expected_type.__name__}")

choose = 1
while(choose > 0):
    print("\033[1mВыберите, что хотите выполнить\033[0m\n" +  "1.Задачу Коши\n" + "2.Система обыкновенных дифференциальных уравнений\n" +
          "3.Уравнение второго порядка;\n" + "4.Модель популяционной системы 'хищник-жертва' (уравнения Лотки и Вольтерры)\n" + "5.GUI\n" + "0.Выход")
    choose = safe_input("", int)
    print("\n" * 5)
    match choose:
        case 1:
            Cauchy_problem.task()
        case 2:
            SODE.task()
        case 3:
            SO_equation.task()
        case 4:
            Predator_Prey.task()
        case 5:
            GUI.task()
        case 0:
            break
        case _:
            print("Такого варианта нет")