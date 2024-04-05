import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SampleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Пример приложения с вкладками")

        self.graphs = {}

        # Создание вкладок
        self.tabControl = ttk.Notebook(self)

        self.CP = ttk.Frame(self.tabControl)
        self.SODE = ttk.Frame(self.tabControl)
        self.SOE = ttk.Frame(self.tabControl)
        self.PP = ttk.Frame(self.tabControl)

        self.tabControl.add(self.CP, text='Задача Коши')
        self.tabControl.add(self.SODE, text='Система обыкновенных дифференциальных уравнений')
        self.tabControl.add(self.SOE, text='Уравнение второго порядка')
        self.tabControl.add(self.PP, text='Система Хищник-Жертва')
        self.tabControl.pack(expand=1, fill="both")

        # Добавление виджетов на первую вкладку
        self.init_CP()  # Инициализация первой вкладки - решение обыкновенных дифференциальных уравнений (ODE)
        self.init_SODE()  # Инициализация второй вкладки - решение систем ОДУ
        self.init_SOE()  # Инициализация третьей вкладки - решение уравнений с отклоняющимся аргументом
        self.init_PP()  # Инициализация четвертой вкладки - решение системы уравнений хищник-жертва

    # Инициализация вкладки для решения обыкновенных дифференциальных уравнений
    def init_CP(self):
        # Ввод функции
        tk.Label(self.CP, text="Введите функцию f(y, t):").pack()
        self.func_entry_CP = tk.Entry(self.CP)
        self.func_entry_CP.pack()
        tk.Label(self.CP, text="y(0):").pack()
        self.y0_entry_CP = tk.Entry(self.CP)
        self.y0_entry_CP.pack()
        tk.Label(self.CP, text="t левая граница:").pack()
        self.t0_entry_CP = tk.Entry(self.CP)
        self.t0_entry_CP.pack()
        tk.Label(self.CP, text="t правая граница:").pack()
        self.t1_entry_CP = tk.Entry(self.CP)
        self.t1_entry_CP.pack()
        tk.Label(self.CP, text="Шаг:").pack()
        self.step_entry_CP = tk.Entry(self.CP)
        self.step_entry_CP.pack()

        # Кнопка для построения графика
        self.plot_button_CP = tk.Button(self.CP, text="Построить график", command=self.plot_graph_CP)
        self.plot_button_CP.pack()
        # Кнопка для очистки графика
        self.plot_delete_CP = tk.Button(self.CP, text="Очистить график", command= lambda: self.clear_graph_by_name('Задача Коши'))
        self.plot_delete_CP.pack()

        # Область для графика
        self.fig_CP, self.ax_CP = plt.subplots(figsize=(12, 10))
        self.canvas_CP = FigureCanvasTkAgg(self.fig_CP, master=self.CP)
        self.canvas_CP.get_tk_widget().pack()
        # В методе init_CP после создания графика
        self.graphs['Задача Коши'] = {'canvas': self.canvas_CP, 'axes': self.ax_CP}

    # Функция для построения графика решения обыкновенных дифференциальных уравнений
    def plot_graph_CP(self):
        try:
            func_str = self.func_entry_CP.get()
            y0_get = float(self.y0_entry_CP.get())
            t0_get = float(self.t0_entry_CP.get())
            t1_get = float(self.t1_entry_CP.get())
            step_get = float(self.step_entry_CP.get())

            def func(y, t):
                return eval(func_str)

            y0 = y0_get
            ti = np.arange(t0_get, t1_get, step_get)
            solution = odeint(func, y0, ti)

            self.ax_CP.clear()
            self.ax_CP.plot(ti, solution, 'r', label=f'y\' = {func_str}')
            self.ax_CP.set_title(f"Решение y\' = {func_str}")
            self.ax_CP.set_xlabel('Время')
            self.ax_CP.set_ylabel('y(t)')
            self.ax_CP.legend()

            self.canvas_CP.draw()
        except ValueError as ve:
            tk.messagebox.showerror("Ошибка значения", f"Произошла ошибка значения: {ve}")
        except SyntaxError as se:
            tk.messagebox.showerror("Синтаксическая ошибка", f"Произошла синтаксическая ошибка: {se}")
        except NameError as ne:
            tk.messagebox.showerror("Ошибка имени", f"Произошла ошибка имени: {ne}")
        except ZeroDivisionError as zde:
            tk.messagebox.showerror("Ошибка деления на ноль", f"Произошла ошибка деления на ноль: {zde}")
        except Exception as e:
            tk.messagebox.showerror("Неизвестная ошибка", f"Произошла неизвестная ошибка: {e}")

    # Инициализация вкладки для решения систем обыкновенных дифференциальных уравнений
    def init_SODE(self):
        # Добавление полей для параметров a, b, c
        tk.Label(self.SODE, text="a:").pack()
        self.entry_a_SODE = tk.Entry(self.SODE)
        self.entry_a_SODE.pack()

        tk.Label(self.SODE, text="b:").pack()
        self.entry_b_SODE = tk.Entry(self.SODE)
        self.entry_b_SODE.pack()

        tk.Label(self.SODE, text="c:").pack()
        self.entry_c_SODE = tk.Entry(self.SODE)
        self.entry_c_SODE.pack()

        tk.Label(self.SODE, text="Уравнение 1:").pack()
        self.entry_y1_SODE = tk.Entry(self.SODE)
        self.entry_y1_SODE.pack()

        tk.Label(self.SODE, text="Уравнение 2:").pack()
        self.entry_y2_SODE = tk.Entry(self.SODE)
        self.entry_y2_SODE.pack()

        tk.Label(self.SODE, text="Уравнение 3:").pack()
        self.entry_y3_SODE = tk.Entry(self.SODE)
        self.entry_y3_SODE.pack()

        # Кнопка для запуска расчета и отображения результатов
        self.solve_button_SODE = tk.Button(self.SODE, text="Построить график", command=self.plot_graph_SODE)
        self.solve_button_SODE.pack()
        # Кнопка для очистки графика
        self.plot_delete_SODE = tk.Button(self.SODE, text="Очистить график",
                                        command=lambda: self.clear_graph_by_name('Система обыкновенных дифференциальных уравнений'))
        self.plot_delete_SODE.pack()

        # Место для отображения графиков
        self.fig_SODE, self.axs_SODE = plt.subplots(2, 2, figsize=(12, 10))
        self.canvas_SODE = FigureCanvasTkAgg(self.fig_SODE, master=self.SODE)
        self.canvas_SODE.get_tk_widget().pack()

        # В методе init_SODE после создания графика
        self.graphs['Система обыкновенных дифференциальных уравнений'] = {'canvas': self.canvas_SODE, 'axes': self.axs_SODE}

    # Функция для построения графиков решения систем обыкновенных дифференциальных уравнений
    def plot_graph_SODE(self):
        try:
            # Чтение и обработка входных данных
            a = float(self.entry_a_SODE.get())
            b = float(self.entry_b_SODE.get())
            c = float(self.entry_c_SODE.get())
            y1_str = self.entry_y1_SODE.get()  # Это строки, содержащие выражения
            y2_str = self.entry_y2_SODE.get()
            y3_str = self.entry_y3_SODE.get()

            # Функция, которая преобразует строки в вычисляемые выражения
            def function(eq, t, a, b, c):
                y1, y2, y3 = eq
                dy1 = eval(y1_str, globals(), locals())
                dy2 = eval(y2_str, globals(), locals())
                dy3 = eval(y3_str, globals(), locals())
                return [dy1, dy2, dy3]

            t = np.arange(0, 100, 0.1)
            y0 = [1.0, 1.0, 1.0]

            # Решение системы уравнений
            solution = odeint(function, y0, t, args=(a, b, c))

            # Очистка предыдущих графиков
            for ax in self.axs_SODE.flatten():
                ax.clear()

            # Отображение новых графиков
            self.axs_SODE[0, 0].plot(solution[:, 0], solution[:, 1])
            self.axs_SODE[0, 0].set_title('Фазовый портрет y от x')
            self.axs_SODE[0, 1].plot(t, solution[:, 0])
            self.axs_SODE[0, 1].set_title('График x от t')
            self.axs_SODE[1, 0].plot(t, solution[:, 1])
            self.axs_SODE[1, 0].set_title('График y от t')
            self.axs_SODE[1, 1].plot(t, solution[:, 2])
            self.axs_SODE[1, 1].set_title('График z от t')

            self.canvas_SODE.draw()
        except ValueError as ve:
            tk.messagebox.showerror("Ошибка значения", f"Произошла ошибка значения: {ve}")
        except SyntaxError as se:
            tk.messagebox.showerror("Синтаксическая ошибка", f"Произошла синтаксическая ошибка: {se}")
        except NameError as ne:
            tk.messagebox.showerror("Ошибка имени", f"Произошла ошибка имени: {ne}")
        except ZeroDivisionError as zde:
            tk.messagebox.showerror("Ошибка деления на ноль", f"Произошла ошибка деления на ноль: {zde}")
        except Exception as e:
            tk.messagebox.showerror("Неизвестная ошибка", f"Произошла неизвестная ошибка: {e}")

    # Инициализация вкладки для решения уравнений с отклоняющимся аргументом
    def init_SOE(self):
        tk.Label(self.SOE, text="Введите уравнение(через y):").pack()
        self.equation_entry_SOE = tk.Entry(self.SOE)
        self.equation_entry_SOE.pack()

        tk.Label(self.SOE, text="Дополнительный аргумент(только a, можно оставить пустым):").pack()
        self.arg_entry_SOE = tk.Entry(self.SOE)
        self.arg_entry_SOE.pack()

        # Кнопка для решения уравнения
        self.solve_button_SOE = tk.Button(self.SOE, text="Построить график", command=self.plot_graph_SOE)
        self.solve_button_SOE.pack()
        # Кнопка для очистки графика
        self.plot_delete_SOE = tk.Button(self.SOE, text="Очистить график",
                                        command=lambda: self.clear_graph_by_name(
                                            'Уравнение второго порядка'))
        self.plot_delete_SOE.pack()

        # Место для графика
        self.fig_SOE, self.ax_SOE = plt.subplots(figsize=(12, 10))
        self.canvas_SOE = FigureCanvasTkAgg(self.fig_SOE, master=self.SOE)
        self.canvas_SOE.get_tk_widget().pack()

        # В методе init_SOE после создания графика
        self.graphs['Уравнение второго порядка'] = {'canvas': self.canvas_SOE, 'axes': self.ax_SOE}

    # Функция для построения графика решения уравнений с отклоняющимся аргументом
    def plot_graph_SOE(self):
        try:
            # Получение уравнения от пользователя
            func_str = self.equation_entry_SOE.get()

            # Преобразование введенного уравнения в функцию
            def function(y, t):
                y1, y2 = y
                dy = eval(func_str, globals(), locals())
                return [y2, dy]

            y0 = [0, 0]
            t = np.arange(0, 2 * np.pi, 0.1)
            solution = odeint(function, y0, t)

            y1, y2 = solution.T

            # Отображение результатов
            self.ax_SOE.clear()
            self.ax_SOE.plot(t, y1, 'b', label='y(t)')
            self.ax_SOE.plot(t, y2, 'g', label='y\'(t)')
            self.ax_SOE.set_title('Решение и производная')
            self.ax_SOE.set_xlabel('Время t')
            self.ax_SOE.set_ylabel('y(t), y\'(t)')
            self.ax_SOE.legend()
            self.canvas_SOE.draw()
        except ValueError as ve:
            tk.messagebox.showerror("Ошибка значения", f"Произошла ошибка значения: {ve}")
        except SyntaxError as se:
            tk.messagebox.showerror("Синтаксическая ошибка", f"Произошла синтаксическая ошибка: {se}")
        except NameError as ne:
            tk.messagebox.showerror("Ошибка имени", f"Произошла ошибка имени: {ne}")
        except ZeroDivisionError as zde:
            tk.messagebox.showerror("Ошибка деления на ноль", f"Произошла ошибка деления на ноль: {zde}")
        except Exception as e:
            tk.messagebox.showerror("Неизвестная ошибка", f"Произошла неизвестная ошибка: {e}")

    # Инициализация вкладки для решения системы уравнений хищник-жертва
    def init_PP(self):
        # Метки и поля ввода для параметров модели
        params = ['r1', 'alpha1', 'alpha2', 'beta2', 'g1', 'x0', 'y0']
        self.entries = {}
        for param in params:
            tk.Label(self.PP, text=f"{param}:").pack()
            entry = tk.Entry(self.PP)
            entry.pack()
            self.entries[param] = entry

        # Кнопка для решения уравнений и отображения результатов
        self.solve_button_PP = tk.Button(self.PP, text="Построить график", command=self.plot_graph_PP)
        self.solve_button_PP.pack()
        # Кнопка для очистки графика
        self.plot_delete_PP = tk.Button(self.PP, text="Очистить график",
                                        command=lambda: self.clear_graph_by_name(
                                            'Система Хищник-Жертва'))
        self.plot_delete_PP.pack()

        # Место для графика
        self.fig_PP, self.axs_PP = plt.subplots(2, 2, figsize=(12, 10))
        self.canvas_PP = FigureCanvasTkAgg(self.fig_PP, master=self.PP)
        self.canvas_PP.get_tk_widget().pack()

        # В методе init_PP после создания графика
        self.graphs['Система Хищник-Жертва'] = {'canvas': self.canvas_PP, 'axes': self.axs_PP}

    # Функция для построения графиков решения системы уравнений хищник-жертва
    def plot_graph_PP(self):
        try:
            # Считывание параметров из полей ввода
            r1 = float(self.entries['r1'].get())
            alpha1 = float(self.entries['alpha1'].get())
            alpha2 = float(self.entries['alpha2'].get())
            beta2 = float(self.entries['beta2'].get())
            g1 = float(self.entries['g1'].get())
            x0 = float(self.entries['x0'].get())
            y0 = float(self.entries['y0'].get())

            initial_state = [x0, y0]
            time = np.arange(0, 1000, 10)

            def predator_prey_system(state, t, r1, alpha1, alpha2, beta2, g1):
                x, y = state
                return [r1 * x - alpha1 * x * y - g1 * x ** 2, alpha2 * x * y - beta2 * y]

            # Решение модели
            solution = odeint(predator_prey_system, initial_state, time, args=(r1, alpha1, alpha2, beta2, g1))
            x, y = solution.T

            # Отображение результатов
            # График плотности популяций во времени
            self.axs_PP[0, 0].clear()
            self.axs_PP[0, 0].plot(time, x, label='Плотность "Жертвы" x(t)')
            self.axs_PP[0, 0].plot(time, y, label='Плотность "Хищника" y(t)')
            self.axs_PP[0, 0].set_title('Плотность населения с течением времени')
            self.axs_PP[0, 0].set_xlabel('Время')
            self.axs_PP[0, 0].set_ylabel('Плотность')
            self.axs_PP[0, 0].legend()

            # Фазовый портрет без конкуренции
            self.axs_PP[0, 1].clear()
            self.axs_PP[0, 1].plot(x, y)
            self.axs_PP[0, 1].set_title('Фазовый портрет без конкуренции')
            self.axs_PP[0, 1].set_xlabel('Плотность "Жертвы" x')
            self.axs_PP[0, 1].set_ylabel('Плотность "Хищника" y')

            # Повторение графиков с "конкуренцией"
            # График плотности популяций во времени с учетом конкуренции
            self.axs_PP[1, 0].clear()
            self.axs_PP[1, 0].plot(time, x, label='Плотность "Жертвы" x(t) с конкуренцией')
            self.axs_PP[1, 0].plot(time, y, label='Плотность "Хищника" y(t) с конкуренцией')
            self.axs_PP[1, 0].set_title('Плотность населения с течением времени с конкуренцией')
            self.axs_PP[1, 0].set_xlabel('Время')
            self.axs_PP[1, 0].set_ylabel('Плотность')
            self.axs_PP[1, 0].legend()

            # Фазовый портрет с учетом конкуренции
            self.axs_PP[1, 1].clear()
            self.axs_PP[1, 1].plot(x, y)
            self.axs_PP[1, 1].set_title('Фазовый портрет с конкуренцией')
            self.axs_PP[1, 1].set_xlabel('Плотность "Жертвы" x с конкуренцией')
            self.axs_PP[1, 1].set_ylabel('Плотность "Хищника" y с конкуренцией')

            self.canvas_PP.draw()
        except ValueError as ve:
            tk.messagebox.showerror("Ошибка значения", f"Произошла ошибка значения: {ve}")
        except SyntaxError as se:
            tk.messagebox.showerror("Синтаксическая ошибка", f"Произошла синтаксическая ошибка: {se}")
        except NameError as ne:
            tk.messagebox.showerror("Ошибка имени", f"Произошла ошибка имени: {ne}")
        except ZeroDivisionError as zde:
            tk.messagebox.showerror("Ошибка деления на ноль", f"Произошла ошибка деления на ноль: {zde}")
        except Exception as e:
            tk.messagebox.showerror("Неизвестная ошибка", f"Произошла неизвестная ошибка: {e}")

    def clear_graph_by_name(self, graph_name):
        # Проверяем, существует ли график с таким названием
        if graph_name in self.graphs:
            graph_info = self.graphs[graph_name]
            graph_info['axes'].clear()  # Очистка осей
            graph_info['canvas'].draw()  # Обновление канваса
        else:
            tk.messagebox.showinfo(f"График с названием '{graph_name}' не найден.")

def task():
    app = SampleApp()
    app.mainloop()