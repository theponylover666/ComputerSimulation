from pulp import LpVariable, LpProblem, LpMaximize, value
import time

start = time.time()
x1 = LpVariable("x1", lowBound=1200)
x2 = LpVariable("x2", lowBound=1000)
x3 = LpVariable("x3", lowBound=1500)
x4 = LpVariable("x4", lowBound=1200)
problem = LpProblem('0', LpMaximize)
problem += 120*x1 + 50*x2 + 30*x3 + 100*x4, "Функция цели"
problem += 18*x1 + 26*x2 + 16 * x3 + 10*x4 <= 110000, "1"
problem += 150*x1 + 140*x2 + 50 * x3 + 80*x4 <= 950000, "2"
problem += 170*x1 + 230*x2 + 280*x3 + 120*x4 <= 1200000, "3"
problem += 31*x1 + 42*x2 + 30*x3 + 20*x4 <= 180000, "4"
problem += 200*x1 + 150*x2 + 170*x3 + 50*x4 >= 750000, "5"
problem.solve()
print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
print("Прибыль:")
print(value(problem.objective))
stop = time.time()
print("Время :")
print(stop - start)
