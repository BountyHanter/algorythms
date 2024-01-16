import random
import time

def sort():
    def quick_sort(arr):
        # Базовый случай: если длина массива меньше или равна 1, он считается отсортированным.
        if len(arr) <= 1:
            return arr

        # Шаг 1: Выбираем опорный элемент случайным образом из массива
        pivot = arr[random.randint(0, len(arr) - 1)]

        # Шаг 2: Разбиваем массив на три подмассива:
        # - less: элементы, меньшие опорного элемента
        # - equal: элементы, равные опорному элементу
        # - greater: элементы, большие опорного элемента
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]

        # Шаг 3: Рекурсивно сортируем подмассивы less и greater
        sorted_less = quick_sort(less)
        sorted_greater = quick_sort(greater)

        # Шаг 4: Собираем отсортированный массив, объединяя less, equal и greater
        sorted_arr = sorted_less + equal + sorted_greater

        return sorted_arr

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            # Флаг, который указывает на то, были ли внутри цикла обмены элементов
            swapped = False
            for j in range(0, n - i - 1):
                # Сравниваем два соседних элемента
                if arr[j] > arr[j + 1]:
                    # Меняем местами элементы, если они находятся в неправильном порядке
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            # Если внутри цикла не было обменов элементов, то список уже отсортирован
            if not swapped:
                break

    random.seed(int(time.time()))
    range_list = [1,5,10,15,20,25,30,35,40,50,60]
    info = {}
    for i in range(len(range_list)):
        arr1 = random.choices(range(1, 1000), k=range_list[i])
        start_time = time.time()
        #print("Замер1 начался")
        quick_sort(arr1)
        end_time = time.time()
        elapsed_time_q = end_time - start_time

        start_time_b = time.time()
        #print("Замер2 начался")
        bubble_sort(arr1)
        end_time_b = time.time()
        elapsed_time_b = end_time_b - start_time_b

        #print("Количество элементов в списке:", len(arr1))
        #print(f"Затраченное время на q сортировку: {elapsed_time_q:.6f} секунд")
        #print(f"Затраченное время на b сортировку: {elapsed_time_b:.6f} секунд")

        info[f'{i}'] = [f'{elapsed_time_q:.6f} ', f'{elapsed_time_b:.6f}']
    return info





