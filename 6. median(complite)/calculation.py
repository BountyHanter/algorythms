import random


def result(data):
    return median(data)


# Функция разделения массива
def partition(arr, low, high):
    # Выбор случайного индекса в пределах low и high
    pivot_index = random.randint(low, high)

    # Перемещение опорного элемента в конец
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]  # Опорный элемент

    i = low - 1  # Индекс для разделения элементов меньше и больше опорного

    # Проход по массиву
    for j in range(low, high):
        # Если текущий элемент меньше или равен опорному, меняем местами с элементом в позиции i+1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Помещаем опорный элемент на свое место (между элементами меньше и больше него)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1  # Возвращаем индекс опорного элемента


# Алгоритм случайного выбора
def randomized_select(arr, low, high, k):
    if low == high:  # Базовый случай: если low и high равны, возвращаем элемент
        return arr[low]

    # Получаем индекс опорного элемента после разделения
    pivot_index = partition(arr, low, high)

    # Если искомый индекс k равен индексу опорного элемента, возвращаем его
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        # Если k меньше индекса опорного элемента, ищем в левой части списка
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        # Если k больше индекса опорного элемента, ищем в правой части списка
        return randomized_select(arr, pivot_index + 1, high, k)


# Функция для нахождения медианы
def median(arr):
    n = len(arr)
    if n % 2 != 0:  # Если количество элементов нечетное
        return randomized_select(arr, 0, n - 1, n // 2)  # Возвращаем элемент посередине
    else:
        # Если количество элементов четное, находим два центральных элемента и находим их среднее значение
        return 0.5 * (randomized_select(arr, 0, n - 1, n // 2 - 1) + randomized_select(arr, 0, n - 1, n // 2))
