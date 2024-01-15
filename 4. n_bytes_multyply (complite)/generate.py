import random

def generate():
    """
    Функция generate() генерирует последовательность пар бинарных чисел, начиная с длины 64 бит и удваивая длину
    при генерации каждой следующей пары чисел. Она создает 7 пар чисел, где каждая следующая пара будет вдвое длиннее
    предыдущей.
    """

    def generate_random_binary(length):
        # Генерация случайного числа длиной length
        return bin(random.getrandbits(length))[2:]


    def generate_pairs(start_length, num_pairs):
        pairs = []
        length = start_length

        for _ in range(num_pairs):
            # Генерация пары чисел с удвоением длины на каждом шаге
            num1 = generate_random_binary(length)
            num2 = generate_random_binary(length)
            pairs.append((num1, num2))

            # Удвоение длины для следующей пары чисел
            length *= 2

        return pairs


    # Генерация пар чисел с длиной начиная с 16 бит и каждая следующая пара длиннее в 2 раза
    return generate_pairs(64, 7)

def generate_more():

    def generate_random_binary(length):
        # Генерация случайного числа длиной length
        return bin(random.getrandbits(length))[2:]


    def generate_pairs(start_length, num_pairs):
        pairs = []
        length = start_length

        for _ in range(num_pairs):
            # Генерация пары чисел с удвоением длины на каждом шаге
            num1 = generate_random_binary(length)
            num2 = generate_random_binary(length)
            pairs.append((num1, num2))

            # Удвоение длины для следующей пары чисел
            length *= 2

        return pairs


    # Генерация пар чисел с длиной начиная с 16 бит и каждая следующая пара длиннее в 2 раза
    return generate_pairs(2056, 10)


