import tkinter as tk
from tkinter import ttk
from Lab3 import Single_channel, Multi_channel

class SMOApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Системы массового обслуживания")
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.single_channel_frame = ttk.Frame(self.notebook)
        self.multi_channel_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.single_channel_frame, text='Одноканальные СМО')
        self.notebook.add(self.multi_channel_frame, text='Многоканальные СМО')
        self.notebook.pack(expand=True, fill='both')

        # Создание вложенных вкладок для одноканальных СМО
        self.single_channel_notebook = ttk.Notebook(self.single_channel_frame)
        self.sc_with_denial_frame = ttk.Frame(self.single_channel_notebook)
        self.sc_with_limited_queue_frame = ttk.Frame(self.single_channel_notebook)
        self.sc_with_unlimited_queue_frame = ttk.Frame(self.single_channel_notebook)
        self.single_channel_notebook.add(self.sc_with_denial_frame, text='С отказами в обслуживании')
        self.single_channel_notebook.add(self.sc_with_limited_queue_frame, text='С ограниченной очередью')
        self.single_channel_notebook.add(self.sc_with_unlimited_queue_frame, text='С неограниченной очередью')
        self.single_channel_notebook.pack(expand=True, fill='both')

        # Создание вложенных вкладок для многоканальных СМО
        self.multi_channel_notebook = ttk.Notebook(self.multi_channel_frame)
        self.mc_with_denial_frame = ttk.Frame(self.multi_channel_notebook)
        self.mc_with_limited_queue_frame = ttk.Frame(self.multi_channel_notebook)
        self.mc_with_unlimited_queue_frame = ttk.Frame(self.multi_channel_notebook)
        self.multi_channel_notebook.add(self.mc_with_denial_frame, text='С отказами в обслуживании')
        self.multi_channel_notebook.add(self.mc_with_limited_queue_frame, text='С ограниченной очередью')
        self.multi_channel_notebook.add(self.mc_with_unlimited_queue_frame, text='С неограниченной очередью')
        self.multi_channel_notebook.pack(expand=True, fill='both')

        # Добавляем виджеты для вложенных вкладок одноканальных СМО
        self.add_sc_with_denial_widgets()
        self.add_sc_with_limited_queue_widgets()
        self.add_sc_with_unlimited_queue_widgets()

        # Добавляем виджеты для вложенных вкладок многоканальных СМО
        self.add_mc_with_denial_widgets()
        self.add_mc_with_limited_queue_widgets()
        self.add_mc_with_unlimited_queue_widgets()

    def add_sc_with_denial_widgets(self):
        # Добавление виджетов для одноканальных СМО с отказами в обслуживании
        ttk.Label(self.sc_with_denial_frame, text="Интенсивность входящего потока:").pack()
        self.sc_lambda_denial_entry = ttk.Entry(self.sc_with_denial_frame)
        self.sc_lambda_denial_entry.pack()

        ttk.Label(self.sc_with_denial_frame, text="Средняя продолжительность обслуживания:").pack()
        self.sc_T_obs_denial_entry = ttk.Entry(self.sc_with_denial_frame)
        self.sc_T_obs_denial_entry.pack()

        sc_denial_calculate_button = ttk.Button(self.sc_with_denial_frame, text="Рассчитать",
                                                command=self.calculate_sc_with_denial)
        sc_denial_calculate_button.pack()

        # Добавляем текстовое поле для вывода результата
        self.result_text_sc_denial = tk.Text(self.sc_with_denial_frame, height=10, width=50)
        self.result_text_sc_denial.pack()

    def calculate_sc_with_denial(self):
        try:
            lambda_ = self.sc_lambda_denial_entry.get().replace(',', '.')
            T_obs = self.sc_T_obs_denial_entry.get().replace(',', '.')

            if not lambda_ or not T_obs:  # Проверяем, не пусты ли поля ввода
                raise ValueError("Одно или оба поля ввода пусты.")

            lambda_float = float(lambda_)
            T_obs_float = float(T_obs)

            if lambda_float <= 0 or T_obs_float <= 0:  # Дополнительная проверка на положительные значения
                raise ValueError("Значения должны быть положительными числами.")

            result = Single_channel.With_Denial_Of_Service(lambda_float, T_obs_float)

            # Обновляем текстовое поле с результатом
            self.result_text_sc_denial.delete('1.0', tk.END)
            self.result_text_sc_denial.insert(tk.END, result)

        except ValueError as e:
            # В случае ошибки очищаем текстовое поле и выводим сообщение об ошибке
            self.result_text_sc_denial.delete('1.0', tk.END)
            self.result_text_sc_denial.insert(tk.END, f"Ошибка: {e}")

    def add_sc_with_limited_queue_widgets(self):
        # Добавление виджетов для одноканальных СМО с ограниченной очередью
        ttk.Label(self.sc_with_limited_queue_frame, text="Длина очереди:").pack()
        self.sc_m_limited_entry = ttk.Entry(self.sc_with_limited_queue_frame)
        self.sc_m_limited_entry.pack()

        ttk.Label(self.sc_with_limited_queue_frame, text="Интенсивность входящего потока:").pack()
        self.sc_lambda_limited_entry = ttk.Entry(self.sc_with_limited_queue_frame)
        self.sc_lambda_limited_entry.pack()

        ttk.Label(self.sc_with_limited_queue_frame, text="Интенсивность обслуживания:").pack()
        self.sc_mu_limited_entry = ttk.Entry(self.sc_with_limited_queue_frame)
        self.sc_mu_limited_entry.pack()

        sc_limited_calculate_button = ttk.Button(self.sc_with_limited_queue_frame, text="Рассчитать",
                                                 command=self.calculate_sc_with_limited)
        sc_limited_calculate_button.pack()

        # Добавляем текстовое поле для вывода результата
        self.result_text_sc_limited = tk.Text(self.sc_with_limited_queue_frame, height=10, width=50)
        self.result_text_sc_limited.pack()

    def calculate_sc_with_limited(self):
        try:
            m = self.sc_m_limited_entry.get().replace(',', '.')
            lambda_ = self.sc_lambda_limited_entry.get().replace(',', '.')
            mu = self.sc_mu_limited_entry.get().replace(',', '.')

            if not m or not lambda_ or not mu:  # Проверяем, не пусты ли поля ввода
                raise ValueError("Одно или оба поля ввода пусты.")

            m_int = int(m)
            lambda_float = float(lambda_)
            mu_float = float(mu)

            if m_int <= 0 or lambda_float <= 0 or mu_float <= 0:  # Дополнительная проверка на положительные значения
                raise ValueError("Значения должны быть положительными числами.")

            result = Single_channel.With_Limited_Queue(m_int, lambda_float, mu_float)

            # Обновляем текстовое поле с результатом
            self.result_text_sc_limited.delete('1.0', tk.END)
            self.result_text_sc_limited.insert(tk.END, result)

        except ValueError as e:
            # В случае ошибки очищаем текстовое поле и выводим сообщение об ошибке
            self.result_text_sc_limited.delete('1.0', tk.END)
            self.result_text_sc_limited.insert(tk.END, f"Ошибка: {e}")

    def add_sc_with_unlimited_queue_widgets(self):
        # Добавление виджетов для одноканальных СМО с неограниченной очередью
        ttk.Label(self.sc_with_unlimited_queue_frame, text="Интенсивность входящего потока:").pack()
        self.sc_lambda_unlimited_entry = ttk.Entry(self.sc_with_unlimited_queue_frame)
        self.sc_lambda_unlimited_entry.pack()

        ttk.Label(self.sc_with_unlimited_queue_frame, text="Средняя продолжительность обслуживания:").pack()
        self.sc_T_obs_unlimited_entry = ttk.Entry(self.sc_with_unlimited_queue_frame)
        self.sc_T_obs_unlimited_entry.pack()

        sc_unlimited_calculate_button = ttk.Button(self.sc_with_unlimited_queue_frame, text="Рассчитать",
                                      command=self.calculate_sc_with_unlimited)
        sc_unlimited_calculate_button.pack()

        # Добавляем текстовое поле для вывода результата
        self.result_text_sc_unlimited = tk.Text(self.sc_with_unlimited_queue_frame, height=10, width=50)
        self.result_text_sc_unlimited.pack()

    def calculate_sc_with_unlimited(self):
        try:
            lambda_ = self.sc_lambda_unlimited_entry.get().replace(',', '.')
            T_obs = self.sc_T_obs_unlimited_entry.get().replace(',', '.')

            if not lambda_ or not T_obs:  # Проверяем, не пусты ли поля ввода
                raise ValueError("Одно или оба поля ввода пусты.")

            lambda_float = float(lambda_)
            T_obs_float = float(T_obs)

            if lambda_float <= 0 or T_obs_float <= 0:  # Дополнительная проверка на положительные значения
                raise ValueError("Значения должны быть положительными числами.")

            result = Single_channel.With_Unlimited_Queue(lambda_float, T_obs_float)

            # Обновляем текстовое поле с результатом
            self.result_text_sc_unlimited.delete('1.0', tk.END)
            self.result_text_sc_unlimited.insert(tk.END, result)

        except ValueError as e:
            # В случае ошибки очищаем текстовое поле и выводим сообщение об ошибке
            self.result_text_sc_unlimited.delete('1.0', tk.END)
            self.result_text_sc_unlimited.insert(tk.END, f"Ошибка: {e}")

    def add_mc_with_denial_widgets(self):
        # Добавление виджетов для многоканальных СМО с отказами в обслуживании
        ttk.Label(self.mc_with_denial_frame, text="Количество каналов обслуживания:").pack()
        self.mc_n_denial_entry = ttk.Entry(self.mc_with_denial_frame)
        self.mc_n_denial_entry.pack()

        ttk.Label(self.mc_with_denial_frame, text="Интенсивность входящего потока:").pack()
        self.mc_lambda_denial_entry = ttk.Entry(self.mc_with_denial_frame)
        self.mc_lambda_denial_entry.pack()

        ttk.Label(self.mc_with_denial_frame, text="Интенсивность обслуживания одним каналом:").pack()
        self.mc_mu_denial_entry = ttk.Entry(self.mc_with_denial_frame)
        self.mc_mu_denial_entry.pack()

        mc_denial_calculate_button = ttk.Button(self.mc_with_denial_frame, text="Рассчитать",
                                                command=self.calculate_mc_with_denial)
        mc_denial_calculate_button.pack()

        # Добавляем текстовое поле для вывода результата
        self.result_text_mc_denial = tk.Text(self.mc_with_denial_frame, height=10, width=50)
        self.result_text_mc_denial.pack()

    def calculate_mc_with_denial(self):
        try:
            n = self.mc_n_denial_entry.get().replace(',', '.')
            lambda_ = self.mc_lambda_denial_entry.get().replace(',', '.')
            mu = self.mc_mu_denial_entry.get().replace(',', '.')

            if not lambda_ or not n or not mu:  # Проверяем, не пусты ли поля ввода
                raise ValueError("Одно или оба поля ввода пусты.")

            n_int = int(n)
            lambda_float = float(lambda_)
            mu_float = float(mu)

            if lambda_float <= 0 or n_int <= 0 or mu_float <= 0:  # Дополнительная проверка на положительные значения
                raise ValueError("Значения должны быть положительными числами.")

            result = Multi_channel.With_Denial_Of_Service(n_int, lambda_float, mu_float)

            # Обновляем текстовое поле с результатом
            self.result_text_mc_denial.delete('1.0', tk.END)
            self.result_text_mc_denial.insert(tk.END, result)

        except ValueError as e:
            # В случае ошибки очищаем текстовое поле и выводим сообщение об ошибке
            self.result_text_mc_denial.delete('1.0', tk.END)
            self.result_text_mc_denial.insert(tk.END, f"Ошибка: {e}")

    def add_mc_with_limited_queue_widgets(self):
        # Добавление виджетов для многоканальных СМО с ограниченной очередью
        ttk.Label(self.mc_with_limited_queue_frame, text="Количество каналов обслуживания:").pack()
        self.mc_n_limited_entry = ttk.Entry(self.mc_with_limited_queue_frame)
        self.mc_n_limited_entry.pack()

        ttk.Label(self.mc_with_limited_queue_frame, text="Длина очереди:").pack()
        self.mc_m_limited_entry = ttk.Entry(self.mc_with_limited_queue_frame)
        self.mc_m_limited_entry.pack()

        ttk.Label(self.mc_with_limited_queue_frame, text="Интенсивность входящего потока:").pack()
        self.mc_lambda_limited_entry = ttk.Entry(self.mc_with_limited_queue_frame)
        self.mc_lambda_limited_entry.pack()

        ttk.Label(self.mc_with_limited_queue_frame, text="Интенсивность обслуживания одним каналом:").pack()
        self.mc_mu_limited_entry = ttk.Entry(self.mc_with_limited_queue_frame)
        self.mc_mu_limited_entry.pack()

        mc_limited_calculate_button = ttk.Button(self.mc_with_limited_queue_frame, text="Рассчитать",
                                                 command=self.calculate_mc_with_limited)
        mc_limited_calculate_button.pack()

        # Добавляем текстовое поле для вывода результата
        self.result_text_mc_limited = tk.Text(self.mc_with_limited_queue_frame, height=10, width=50)
        self.result_text_mc_limited.pack()

    def calculate_mc_with_limited(self):
        try:
            n = self.mc_n_limited_entry.get().replace(',', '.')
            m = self.mc_m_limited_entry.get().replace(',', '.')
            lambda_ = self.mc_lambda_limited_entry.get().replace(',', '.')
            mu = self.mc_mu_limited_entry.get().replace(',', '.')

            if not m or not lambda_ or not mu or not n:  # Проверяем, не пусты ли поля ввода
                raise ValueError("Одно или оба поля ввода пусты.")

            n_int = int(n)
            m_int = int(m)
            lambda_float = float(lambda_)
            mu_float = float(mu)

            if m_int <= 0 or lambda_float <= 0 or mu_float <= 0 or n_int <= 0:  # Дополнительная проверка на положительные значения
                raise ValueError("Значения должны быть положительными числами.")

            result = Multi_channel.With_Limited_Queue(n_int, m_int, lambda_float, mu_float)

            # Обновляем текстовое поле с результатом
            self.result_text_mc_limited.delete('1.0', tk.END)
            self.result_text_mc_limited.insert(tk.END, result)

        except ValueError as e:
            # В случае ошибки очищаем текстовое поле и выводим сообщение об ошибке
            self.result_text_mc_limited.delete('1.0', tk.END)
            self.result_text_mc_limited.insert(tk.END, f"Ошибка: {e}")

    def add_mc_with_unlimited_queue_widgets(self):
        ttk.Label(self.mc_with_unlimited_queue_frame, text="Количество каналов обслуживания:").pack()
        self.mc_n_unlimited_entry = ttk.Entry(self.mc_with_unlimited_queue_frame)
        self.mc_n_unlimited_entry.pack()

        ttk.Label(self.mc_with_unlimited_queue_frame, text="Интенсивность входящего потока:").pack()
        self.mc_lambda_unlimited_entry = ttk.Entry(self.mc_with_unlimited_queue_frame)
        self.mc_lambda_unlimited_entry.pack()

        ttk.Label(self.mc_with_unlimited_queue_frame, text="Интенсивность обслуживания одним каналом:").pack()
        self.mc_mu_unlimited_entry = ttk.Entry(self.mc_with_unlimited_queue_frame)
        self.mc_mu_unlimited_entry.pack()

        mc_unlimited_calculate_button = ttk.Button(self.mc_with_unlimited_queue_frame, text="Рассчитать",
                                                   command=self.calculate_mc_with_unlimited)
        mc_unlimited_calculate_button.pack()

        # Добавляем текстовое поле для вывода результата
        self.mc_unlimited_result_text = tk.Text(self.mc_with_unlimited_queue_frame, height=10, width=50)
        self.mc_unlimited_result_text.pack()

    def calculate_mc_with_unlimited(self):
        try:
            n = self.mc_n_unlimited_entry.get().replace(',', '.')
            lambda_ = self.mc_lambda_unlimited_entry.get().replace(',', '.')
            mu = self.mc_mu_unlimited_entry.get().replace(',', '.')

            if not lambda_ or not n or not mu:  # Проверяем, не пусты ли поля ввода
                raise ValueError("Одно или оба поля ввода пусты.")

            n_int = int(n)
            lambda_float = float(lambda_)
            mu_float = float(mu)

            if lambda_float <= 0 or n_int <= 0 or mu_float <= 0:  # Дополнительная проверка на положительные значения
                raise ValueError("Значения должны быть положительными числами.")

            result = Multi_channel.With_Unlimited_Queue(n_int, lambda_float, mu_float)

            # Обновляем текстовое поле с результатом
            self.mc_unlimited_result_text.delete('1.0', tk.END)
            self.mc_unlimited_result_text.insert(tk.END, result)

        except ValueError as e:
            # В случае ошибки очищаем текстовое поле и выводим сообщение об ошибке
            self.mc_unlimited_result_text.delete('1.0', tk.END)
            self.mc_unlimited_result_text.insert(tk.END, f"Ошибка: {e}")

app = SMOApplication()
app.mainloop()