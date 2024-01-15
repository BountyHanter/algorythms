"""import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import q_vs_b


#  Мой словарь
data = q_vs_b.sort()

# Количество элементов при каждой сортировке
num_elements = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60]

# Извлечение времени сортировки для первого и второго алгоритма
time_algorithm1 = [float(value[0]) for value in data.values()]
time_algorithm2 = [float(value[1]) for value in data.values()]

# Построение графика с двумя линиями разного цвета
plt.plot(num_elements, time_algorithm1, label='Алгоритм быстрой сортировки', marker='o', color='blue')
plt.plot(num_elements, time_algorithm2, label='Алгоритм пузырьковой сортировки', marker='s', color='red')

plt.xlabel('Количество элементов')
plt.ylabel('Время сортировки (сек)')
plt.title('Зависимость времени от количества элементов')
plt.legend()

# Отображение графика
plt.show()"""
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import q_vs_b
import math
import numpy as np

# Мой словарь
data = q_vs_b.sort()

# Количество элементов при каждой сортировке
num_elements = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60]

# Извлечение времени сортировки для первого и второго алгоритма
time_algorithm1 = [float(value[0]) for value in data.values()]
time_algorithm2 = [float(value[1]) for value in data.values()]

# График n^2
n_squared = [(n ** 2) for n in num_elements]
n_log_n = [(n * math.log(n)) for n in num_elements]
n_log_n[0] = 1
print(time_algorithm2)
print(n_squared)


# Вычисление отношения пузырьковой сортировки к n^2
attitude = [(t2 / n2) for t2, n2 in zip(time_algorithm2, n_squared)]
attitude1 = [(t1/n) for t1, n in zip(time_algorithm1, n_log_n)]
print(attitude1)

# Построение графика для первых двух линий
fig, ax1 = plt.subplots()
ax1.plot(num_elements, time_algorithm1, label='Алгоритм быстрой сортировки', marker='o', color='blue')
ax1.plot(num_elements, time_algorithm2, label='Алгоритм пузырьковой сортировки', marker='s', color='red')
ax1.set_xlabel('Количество элементов')
ax1.set_ylabel('Время сортировки (сек*100000)', color='black')
ax1.legend(loc='upper left')

num_elements=num_elements[3:]
attitude=attitude[3:]
n_log_n = n_log_n[3:]
attitude1 = attitude1[3:]

# Создание отдельного графика для третьей линии
fig, ax2 = plt.subplots()
ax2.plot(num_elements, attitude, label='Отношение пузырьковой к n^2', marker='^', color='green')
ax2.set_xlabel('Количество элементов')
ax2.set_ylabel('Отношение', color='black')
ax2.set_title('Отношение пузырьковой сортировки к n^2')
ax2.legend(loc='upper left')

fig, ax3 = plt.subplots()
ax3.plot(num_elements, attitude1, label='Отношение быстрой к nlog(n)', marker='^', color='green')
ax3.set_xlabel('Количество элементов')
ax3.set_ylabel('Отношение', color='black')
ax3.set_title('Отношение быстрой сортировки к nlog(n)')
ax3.legend(loc='upper left')

plt.show()
