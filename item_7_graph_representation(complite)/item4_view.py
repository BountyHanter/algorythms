import random
import item1_many_vertices_and_edges as vae, item2_adjacency_matrix as am, item3_adjecency_list as al, time
import matplotlib.pyplot as plt


def vae_times():
    random.seed(time.time())
    graph_list = []
    elem = []
    elem_sqr = []
    time_list = []
    time_find_list = []
    count_edges = []
    for i in range(1,6):
        start_time = time.time()
        graph = vae.GraphSet.generate_graph(i*250, i*125)
        graph_list.append(graph)
        elem.append(i*250)
        elem_sqr.append((i*250)**2)
        end_time = time.time()
        result_time = end_time - start_time
        time_list.append(result_time)
        count_edges.append(graph.count_edges())
        start_time = time.time()
        graph.edge_exists((random.randint(1, i*250),(random.randint(1, i*250))))
        end_time = time.time()
        result_time = end_time - start_time
        time_find_list.append(result_time)
        print(f"Выполнено {i} из {5}")

    attitude = [(t / e) for t, e in zip(time_list, elem_sqr)]

    plt.figure(figsize=(8, 5))
    plt.plot( elem, time_list, marker='o', linestyle='-', color='m')
    plt.title('Отношение времени генерации графов к кол-ву вершин')
    plt.xlabel('Количество вершин')
    plt.ylabel('Время(сек.)')
    plt.grid(True)

    plt.figure(figsize=(8, 5))
    plt.plot(elem, attitude, marker='o', linestyle='-', color='m')
    plt.title('Отношение времени выполнения к n^2')
    plt.xlabel('Количество чисел')
    plt.ylabel('Отношение')
    plt.grid(True)

    plt.figure(figsize=(8, 5))
    plt.plot( count_edges, time_find_list, marker='o', linestyle='-', color='m')
    plt.title('Отношение времени поиска рёбер к кол-ву рёбер')
    plt.xlabel('Количество вершин')
    plt.ylabel('Время(сек.)')
    plt.grid(True)

    plt.show()


def am_times():
    graph_list = []
    elem = []
    elem_sqr = []
    time_list = []
    for i in range(1,6):
        start_time = time.time()
        graph = am.AdjacencyMatrixGraph(i*250, i*125)
        graph_list.append(graph)
        elem.append(i*250)
        elem_sqr.append((i*250)**2)
        end_time = time.time()
        result_time = end_time - start_time
        time_list.append(result_time)
        print(f"Выполнено {i} из {5}, время {result_time}")

    attitude = [(t / n) for t, n in zip(time_list, elem_sqr)]

    plt.figure(figsize=(8, 5))
    plt.plot( elem, time_list, marker='o', linestyle='-', color='m')
    plt.title('Отношение времени генерации графов к кол-ву вершин')
    plt.xlabel('Количество вершин')
    plt.ylabel('Время(сек.)')
    plt.grid(True)

    plt.figure(figsize=(8, 5))
    plt.plot(elem, attitude, marker='o', linestyle='-', color='m')
    plt.title('Отношение времени выполнения к n^2')
    plt.xlabel('Количество чисел')
    plt.ylabel('Отношение')
    plt.grid(True)

    plt.show()


def all_times():
    random.seed(time.time())
    graph_list = []
    elem = []
    edges = []
    edges_count = []
    time_list = []
    find_time = []
    for i in range(1,6):
        start_time = time.time()
        graph = al.AdjacencyListGraph(i*250, i*125)
        graph_list.append(graph)
        edges.append(graph.count_edges())
        elem.append(i*250)
        end_time = time.time()
        result_time = end_time - start_time
        time_list.append(result_time)
        start_time = time.time()
        graph.edge_exists((random.randint(1, i*250),(random.randint(1, i*250))))
        end_time = time.time()
        result_time = end_time - start_time
        find_time.append(result_time)
        edges_count.append(graph.count_edges())
        print(f"Выполнено {i} из {5}")

    attitude = [(t / (e+ed)) for t, e, ed in zip(time_list, elem, edges)]
    attitude_find = [(t/ed) for t, ed in zip(find_time, edges_count)]

    plt.figure(figsize=(8, 5))
    plt.plot( elem, time_list, marker='o', linestyle='-', color='m')
    plt.title('Отношение времени генерации графов к кол-ву вершин')
    plt.xlabel('Количество вершин')
    plt.ylabel('Время(сек.)')
    plt.grid(True)

    plt.figure(figsize=(8, 5))
    plt.plot(elem, attitude, marker='o', linestyle='-', color='m')
    plt.title('Отношение времени выполнения к n+m')
    plt.xlabel('Количество чисел')
    plt.ylabel('Отношение')
    plt.grid(True)

    plt.figure(figsize=(8, 5))
    plt.plot(edges_count, find_time, marker='o', linestyle='-', color='m')
    plt.title('Отношение времени поиска ребра к кол-ву рёбер')
    plt.xlabel('Количество рёбер')
    plt.ylabel('Время(сек.)')
    plt.grid(True)

    plt.figure(figsize=(8, 5))
    plt.plot(edges_count, attitude_find, marker='o', linestyle='-', color='m')
    plt.title('Отношение времени поиска ребра к n')
    plt.xlabel('Количество рёбер')
    plt.ylabel('Время(сек.)')
    plt.grid(True)

    plt.show()


all_times()