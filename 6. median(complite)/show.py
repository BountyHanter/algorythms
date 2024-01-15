import calculation
import time
import json
import matplotlib.pyplot as plt


import random

# result = []
# for i in range(100000,1000000,100000):
#     g = random.sample(range(1000001), i)
#     result.append(g)
#
# # Запись сгенерированных списков в файл JSON
# with open('lists.json', 'w') as file:
#     json.dump(result, file)

with open('lists.json', 'r') as file:
    result = json.load(file)


sizes = [len(inner_list) for inner_list in result]
print(sizes)

info = {}

for i in range(len(result)):
    start_time = time.time()
    calculation.result(result[i])
    end_time = time.time()
    result_time = end_time - start_time
    info[sizes[i]] = result_time
    print(result_time)

print(info)

com = [value / key for key, value in info.items()]

plt.figure(figsize=(8, 5))
plt.plot(info.keys(), info.values(), marker='o', linestyle='-', color='m')
plt.title('Поиск медиданы: вроятностный алгоритим')
plt.xlabel('Количество чисел')
plt.ylabel('Время (сек.)')
plt.grid(True)

plt.figure(figsize=(8, 5))
plt.plot( info.keys(), com, marker='o', linestyle='-', color='m')
plt.title('Отношение времени выполнения к n')
plt.xlabel('Количество чисел')
plt.ylabel('Отношение')
plt.grid(True)


plt.show()