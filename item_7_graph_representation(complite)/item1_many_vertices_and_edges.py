import random
import time

import matplotlib.pyplot as plt
import networkx as nx


class GraphSet:
    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, edge):
        self.edges.add(edge)

    def edge_exists(self, edge):
        # Проверяем, существует ли ребро
        return edge in self.edges

    def count_edges(self):
        return len(self.edges)

    def __str__(self):
        return f"Рёбра: {self.vertices}\nВершины: {self.edges}"

    def visualize_graph(self):
        graph = nx.Graph()

        for edge in self.edges:
            graph.add_edge(edge[0], edge[1])

        nx.draw(graph, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold', font_size=12)
        plt.show()

    def to_adjacency_matrix(self):
        # Создаем пустую матрицу смежности
        adjacency_matrix = [[0 for _ in range(len(self.vertices))] for _ in range(len(self.vertices))]

        # Заполняем матрицу смежности
        for edge in self.edges:
            # Устанавливаем соответствующие ячейки в матрице смежности в 1
            adjacency_matrix[edge[0]][edge[1]] = 1
            adjacency_matrix[edge[1]][edge[0]] = 1

        for row in adjacency_matrix:
            print(row)
        return adjacency_matrix

    def to_adjacency_list(self):
        # Создаем пустой список смежности
        adjacency_list = {vertex: [] for vertex in self.vertices}

        # Заполняем список смежности
        for edge in self.edges:
            # Добавляем вершины в список смежности для каждого ребра
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])

        for vertex, edges in adjacency_list.items():
            print(f"{vertex}: {edges}")
        return adjacency_list

    @staticmethod
    def generate_graph(num_vertices: int, max_edges_per_vertex: int):
        """
        :param num_vertices: количество вершин
        :param max_edges_per_vertex: количество рёбер для каждой вершины (если значение меньше чем количество вершин,
                                     то есть вероятность, что некоторые вершины останутся без рёбер)
        :return: готовый граф
        """
        graph = GraphSet()
        edge_counts = [0] * num_vertices  # Счетчик ребер для каждой вершины

        # Добавляем вершины в граф
        for i in range(num_vertices):
            graph.add_vertex(i)

        for i in range(num_vertices):
            # Создаем список вершин, кроме текущей, чтобы избежать ссылки на саму себя
            possible_edges = list(range(num_vertices))
            possible_edges.remove(i)

            random.shuffle(possible_edges)

            for edge in possible_edges:
                # Проверяем, существует ли уже ребро или его обратное
                if not graph.edge_exists((i, edge)) and not graph.edge_exists((edge, i)):
                    # Проверяем, не превышено ли максимальное количество ребер для обеих вершин
                    if edge_counts[i] < max_edges_per_vertex and edge_counts[edge] < max_edges_per_vertex:
                        graph.add_edge((i, edge))
                        edge_counts[i] += 1
                        edge_counts[edge] += 1

        return graph



