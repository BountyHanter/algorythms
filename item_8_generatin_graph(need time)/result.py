import matplotlib.pyplot as plt
import networkx as nx
import random


def full_graph():
    def generate_full_graphs(n, m):
        """
        Генерирует m полных графов с общим количеством n вершин.
        Возвращает список матриц смежности.
        """
        if n < m:
            raise ValueError("Количество вершин должно быть больше или равно количеству связных компонент")

        # Количество вершин в каждом графе
        vertices_per_graph = [n // m + (1 if i < n % m else 0) for i in range(m)]

        adjacency_matrices = []
        for vertices in vertices_per_graph:
            # Создаем матрицу vertices x vertices, заполненную нулями
            adjacency_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

            # Добавляем ребра в матрицу смежности
            for i in range(vertices):
                for j in range(i + 1, vertices):
                    adjacency_matrix[i][j] = 1
                    adjacency_matrix[j][i] = 1

            adjacency_matrices.append(adjacency_matrix)

        return adjacency_matrices

    def draw_graphs(adjacency_matrices):
        """
        Рисует графы на основе списка матриц смежности.
        Все графы выводятся в одном окне.
        """
        G = nx.Graph()
        offset = 0
        for adjacency_matrix in adjacency_matrices:
            n = len(adjacency_matrix)
            # Добавляем все вершины в граф
            G.add_nodes_from(range(offset, offset + n))
            for i in range(n):
                for j in range(i + 1, n):
                    if adjacency_matrix[i][j] == 1:
                        G.add_edge(i + offset, j + offset)
            offset += n
        pos = nx.spring_layout(G)  # используем алгоритм spring_layout для расположения вершин
        nx.draw(G, pos, with_labels=True)
        plt.show()

    # Пример использования:
    n = int(input("Введите общее количество вершин: "))
    m = int(input("Введите количество связных компонент: "))
    adjacency_matrices = generate_full_graphs(n, m)
    for i, adjacency_matrix in enumerate(adjacency_matrices):
        print(f"Матрица смежности для графа {i + 1}:")
        print(adjacency_matrix)

    draw_graphs(adjacency_matrices)


def sparse_graph():
    def generate_graph(num_vertices, num_components):
        if num_vertices < num_components * 4:
            raise ValueError("Недостаточно вершин для создания указанного числа компонент")

        vertices_per_component = num_vertices // num_components
        remaining_vertices = num_vertices % num_components

        graph = {i: [] for i in range(num_vertices)}

        for i in range(num_components):
            start = i * vertices_per_component
            end = (i + 1) * vertices_per_component
            if i == num_components - 1:
                end += remaining_vertices

            for vertex in range(start, end):
                if vertex != start:  # Don't connect the first vertex to anything
                    parent_vertex = random.choice(
                        range(start, vertex))  # Connect to any previous vertex in the same component
                    graph[vertex].append(parent_vertex)
                    graph[parent_vertex].append(vertex)

        return graph

    def draw_graph(graph):
        G = nx.Graph(graph)
        nx.draw(G, with_labels=True)
        plt.show()

    n = int(input("Введите общее количество вершин: "))
    m = int(input("Введите количество связных компонент: "))
    result = generate_graph(n, m)
    print(result)
    draw_graph(result)

sparse_graph()