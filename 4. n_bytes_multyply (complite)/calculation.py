import generate
from decimal import Decimal, getcontext
def binary_multiplication(num1, num2):
    # Реверсирование строк для удобства работы с меньшими разрядами
    num1 = num1[::-1]
    num2 = num2[::-1]

    # Инициализация массива для хранения промежуточных результатов умножения
    products = [0] * (len(num1) + len(num2))

    # Умножение в столбик
    for i in range(len(num1)):
        for j in range(len(num2)):
            products[i + j] += int(num1[i]) * int(num2[j])

    # Выполнение переносов
    carry = 0
    result = ''
    for digit in products:
        digit += carry
        result += str(digit % 2) # добавляет в строку result остаток от деления на 2 значения digit.
        # Это означает, что мы добавляем в результат значение, соответствующее одному биту - либо 0, либо 1.
        carry = digit // 2
        # вычисляет новое значение переноса для следующего разряда путём деления на 2 значения digit.
        # Это новое значение будет использоваться при следующей итерации цикла для корректного выполнения переносов.


    # Удаление ведущих нулей
    result = result.rstrip('0')

    # Если результат пустой, значит умножение было на 0
    if result == '':
        return '0'

    # Инвертирование строки, чтобы получить корректный порядок битов
    return result[::-1]


#num1 = '101011'
#num2 = '1111'

#result = binary_multiplication(num1, num2)
#print(result)


def naive_recursive(num1, num2):
    # Функция для сдвига числа влево на указанное количество битов
    def left_shift(bin_num, shift):
        return bin_num + '0' * shift

    # Функция для сдвига числа вправо на указанное количество битов
    def right_shift(bin_num, shift):
        return bin_num[:-shift]

    # Функция для складывания двух двоичных чисел
    def add_binary(bin_num1, bin_num2):
        return bin(int(bin_num1, 2) + int(bin_num2, 2))[2:]

    # Нахождение максимальной длины числа и дополнение нулями до равной длины
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    result = '0'
    # сдвигаем и складываем - это имитация умножения
    for i in range(len(num1)):
        if num1[-1] == '1':
            result = add_binary(result, left_shift(num2, i))
        num1 = right_shift(num1, 1)

    return result


"""
# Тест
num1 = '1010' 
num2 = '1111' 

print(multiply_recursive(num1, num2)) 
"""

def karatsuba(num1, num2):
    n = max(len(num1), len(num2))

    # Базовый случай: если числа состоят из одного бита
    if n == 1:
        return int(num1, 2) * int(num2, 2)

    # Вычисление половины длины
    n_half = n // 2
    a, b = num1[:-n_half], num1[-n_half:]
    c, d = num2[:-n_half], num2[-n_half:]

    # Дополнение нулями слева, если длины чисел не равны
    if len(a) != len(c):
        max_len = max(len(a), len(c))
        a = a.zfill(max_len)
        c = c.zfill(max_len)
    if len(b) != len(d):
        max_len = max(len(b), len(d))
        b = b.zfill(max_len)
        d = d.zfill(max_len)

    # Рекурсивные вызовы для половин чисел
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(bin(int(a, 2) + int(b, 2))[2:], bin(int(c, 2) + int(d, 2))[2:]) - ac - bd

    # Вычисление результата по формуле Карацубы
    result = (ac << (2 * n_half)) + (ad_plus_bc << n_half) + bd
    return result

"""
# Тест
num1 = '1010' 
num2 = '1111'
"""

# nums = generate.generate()
#print(multiply_recursive(nums[6][0], nums[6][1]))