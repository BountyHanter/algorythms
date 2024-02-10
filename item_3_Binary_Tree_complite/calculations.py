import Tree
import time
import matplotlib
import random


# создаем список для n значений
n_node = [i for i in range(50000, 250001,50000)]


def generate_random_list(size):
    current_time = int(time.time())
    random.seed(current_time)
    random_list = random.sample(range(1,500001), size)
    return random_list


def time_insert():
    print('Выполняется вставка')
    time_insert_result = {}
    total_iterations = len(n_node)
    for index, i in enumerate(n_node, start=1):
        values_list = generate_random_list(i)
        tree = Tree.BinaryTree(500)
        start_time = time.time()
        for value in values_list:
            tree.insert(value)
        end_time = time.time()
        result = end_time - start_time
        time_insert_result[i] = result
        print(f"Выполнено {index} из {total_iterations}")
    return time_insert_result


# Время очень маленькое, там с десяток операций всего лишь
def time_search():
    print("Выполняется поиск")
    time_search_result = {}
    total_iterations = len(n_node)
    for index, i in enumerate(n_node, start=1):
        values_list = generate_random_list(i)
        tree = Tree.BinaryTree(500)
        for value in values_list:
            tree.insert(value)
        start_time = time.time()
        tree.search(random.choice(values_list))
        end_time = time.time()
        #print(start_time, end_time)
        result = end_time - start_time
        print(result)
        time_search_result[i] = result
        print(f"Выполнено {index} из {total_iterations}")
    return time_search_result


def time_search_max_depth():
    print("Выполняется поиск макс глубины")
    time_search_max_depth_result = {}
    total_iterations = len(n_node)
    for index, i in enumerate(n_node, start=1):
        values_list = generate_random_list(i)
        tree = Tree.BinaryTree(500)
        for value in values_list:
            tree.insert(value)
        start_time = time.time()
        tree.max_depth()
        end_time = time.time()
        result = end_time - start_time
        print(result)
        time_search_max_depth_result[i] = result
        print(f"Выполнено {index} из {total_iterations}")
    return time_search_max_depth_result
