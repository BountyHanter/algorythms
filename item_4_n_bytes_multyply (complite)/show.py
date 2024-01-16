import matplotlib.pyplot as plt
import times


results = [times.time_binary_multiplication(), times.time_multiply_recursive(), times.time_karatsuba()]

bits_count = [list(results[0].keys()), list(results[1].keys()), list(results[2].keys())]
times_values = [list(results[0].values()), list(results[1].values()), results[2].values()]


# Вычисление отношения времени к количеству бит
time_per_bit = [
    [time / bits for bits, time in zip(bits_count[0], times_values[0])],
    [time / bits for bits, time in zip(bits_count[1], times_values[1])],
    [time / bits for bits, time in zip(bits_count[2], times_values[2])],
    ]

# Отношение для вычисления смложности
algorithm_complexity = [
    [time / bits**2 for bits, time in zip(bits_count[0], times_values[0])],
    [time / bits**2 for bits, time in zip(bits_count[1], times_values[1])],
    [time / bits**1.59 for bits, time in zip(bits_count[2], times_values[2])],
    ]

# График отношения времени к количеству бит
plt.figure(figsize=(8, 5))
plt.plot(bits_count[0], times_values[0], marker='o', linestyle='-', color='m')
plt.title('Отношение времени вычисления к количеству бит (столбиком)')
plt.xlabel('Количество бит')
plt.ylabel('Время (сек.)')
plt.grid(True)

plt.figure(figsize=(8, 5))
plt.plot(bits_count[1], times_values[1], marker='o', linestyle='-', color='m')
plt.title('Отношение времени вычисления к количеству бит (наивный улучшенный)')
plt.xlabel('Количество бит')
plt.ylabel('Время (сек.)')
plt.grid(True)

plt.figure(figsize=(8, 5))
plt.plot(bits_count[2], times_values[2], marker='o', linestyle='-', color='m')
plt.title('Отношение времени вычисления к количеству бит (Каратусба)')
plt.xlabel('Количество бит')
plt.ylabel('Время (сек.)')
plt.grid(True)


plt.figure(figsize=(8, 5))
plt.plot(bits_count[0], algorithm_complexity[0], marker='o', linestyle='-', color='m')
plt.title('Отношение времени к n^2 (столбик)')
plt.xlabel('Количество бит')
plt.ylabel('Время (сек.) / n^2')
plt.grid(True)

plt.figure(figsize=(8, 5))
plt.plot(bits_count[1], algorithm_complexity[1], marker='o', linestyle='-', color='m')
plt.title('Отношение времени к n^2 (наивный)')
plt.xlabel('Количество бит')
plt.ylabel('Время (сек.) / n^2')
plt.grid(True)

plt.figure(figsize=(8, 5))
plt.plot(bits_count[2], algorithm_complexity[2], marker='o', linestyle='-', color='m')
plt.title('Отношение времени к n^1.59 (карацуба)')
plt.xlabel('Количество бит')
plt.ylabel('Время (сек.) / n^1.59')
plt.grid(True)


plt.show()
