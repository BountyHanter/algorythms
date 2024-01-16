import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def sort():
    def fibonacci_naive(n):
        if n <= 1:
            return n
        return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

    def fibonacci_memoization(n):
        def fib(n, memo={}):
            if n in memo:
                return memo[n]
            if n <= 1:
                memo[n] = n
            else:
                memo[n] = fib(n - 1) + fib(n - 2)
            return memo[n]

        return fib(n)

    # Создадим список значений n для эксперимента
    n_values = [5, 10, 15, 20, 25, 30]
    n_values2 = list(range(5, 150, 10))

    # Измерим время выполнения для каждого значения n
    info1 = {}
    for n in n_values:
        start_time = time.time()
        fibonacci_naive(n)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"n = {n}, Время выполнения (Наивный метод): {elapsed_time:.6f} секунд")
        info1[n] = elapsed_time

    info2 = {}
    print("\nМемоизация\n")
    for n in n_values2:
        start_time = time.time()
        fibonacci_memoization(n)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"n = {n}, Время выполнения (Мемоизация): {elapsed_time:.6f} секунд")
        info2[n] = elapsed_time

    # Преобразование словарей в два списка: значения n и времена выполнения
    n_values1 = list(info1.keys())
    elapsed_times1 = list(info1.values())

    n_values2 = list(info2.keys())
    elapsed_times2 = list(info2.values())

    # Рассчитываем 2^n для каждого значения n из n_values
    n_exp = [2 ** n for n in n_values]

    # Вычисляем отношение времени выполнения к 2^n для каждого значения n
    compl_naive = [elapsed / exp for elapsed, exp in zip(elapsed_times1, n_exp)]
    compl_memo = [time / values for time, values in zip(elapsed_times2,n_values2)]

    # Построение первого графика
    plt.figure(1)
    plt.plot(n_values1, elapsed_times1, marker='o')
    plt.xlabel('Количество элементов')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Зависимость времени выполнения от количества элементов (Наивный метод)')
    plt.grid(True)

    # Построение второго графика
    plt.figure(2)
    plt.plot(n_values2, elapsed_times2, marker='o', color='orange')
    plt.xlabel('Количество элементов')
    plt.ylabel('Время выполнения')
    plt.title('Зависимость времени выполнения от количества элементов (Мемоизация)')
    plt.grid(True)


    # Построение третьего графика

    plt.figure(3)
    plt.plot(n_values1, compl_naive, marker='o', color='orange')
    plt.xlabel('Количество элементов')
    plt.ylabel('Отношение')
    plt.title('Отношение наивного метода к 2^n')
    plt.grid(True)

    # Построение 4го графика

    plt.figure(4)
    plt.plot(n_values2, compl_memo, marker='o', color='orange')
    plt.xlabel('Количество элементов')
    plt.ylabel('Отношение')
    plt.title('Отношение мемоизации к линейной')
    plt.grid(True)



    # Отображение обоих графиков в отдельных окнах
    plt.show()

sort()
