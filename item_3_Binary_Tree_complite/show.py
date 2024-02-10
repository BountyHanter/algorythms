import matplotlib.pyplot as plt
import calculations
from math import log

# Измерения времени вставки элементов
time_insert_result = calculations.time_insert()

print(time_insert_result)

# Измерения времени поиска максимальной глубины
time_search_max_depth_result = calculations.time_search_max_depth()

# Измерения времени поиска элемента
time_search_element = calculations.time_search()

# Создание списков для данных графиков отношения
n_insert = [value / key for key, value in time_insert_result.items()]
n_max_depth = [value / key for key, value in time_search_max_depth_result.items()]
log_n_search = [value / log(key) for key, value in time_search_element.items()]

# График времени вставки элементов
plt.figure(figsize=(8, 5))
plt.plot(list(time_insert_result.keys()), list(time_insert_result.values()), marker='o', linestyle='-', color='b')
plt.title('Зависимость времени вставки от количества элементов')
plt.xlabel('Количество элементов')
plt.ylabel('Время (сек)')
plt.grid(True)

# График времени поиска максимальной глубины
plt.figure(figsize=(8, 5))
plt.plot(list(time_search_max_depth_result.keys()), list(time_search_max_depth_result.values()), marker='o', linestyle='-', color='r')
plt.title('Зависимость времени поиска максимальной глубины от количества элементов')
plt.xlabel('Количество элементов')
plt.ylabel('Время (сек)')
plt.grid(True)

# График времени вставки элементов относительно n
plt.figure(figsize=(8, 5))
plt.plot(list(time_insert_result.keys()), n_insert, marker='o', linestyle='-', color='g')
plt.title('Отношение времени вставки к n')
plt.xlabel('Количество элементов')
plt.ylabel('Время / n')
plt.grid(True)

# График времени поиска максимальной глубины относительно n
plt.figure(figsize=(8, 5))
plt.plot(list(time_search_max_depth_result.keys()), n_max_depth, marker='o', linestyle='-', color='m')
plt.title('Отношение времени поиска максимальной глубины к n')
plt.xlabel('Количество элементов')
plt.ylabel('Время / n')
plt.grid(True)

plt.figure(figsize=(8, 5))
plt.plot(list(time_search_element.keys()), list(time_search_element.values()), marker='o', linestyle='-', color='m')
plt.title('Зависимость времени поиска от кол-ва элементов')
plt.xlabel('Количество элементов')
plt.ylabel('Время(сек)')
plt.grid(True)

plt.figure(figsize=(8, 5))
plt.plot(list(time_search_element.keys()), log_n_search, marker='o', linestyle='-', color='m')
plt.title('Отношение времени поиска элемента к log n')
plt.xlabel('Количество элементов')
plt.ylabel('Время / log n')
plt.grid(True)

# Показать оба графика
plt.show()
