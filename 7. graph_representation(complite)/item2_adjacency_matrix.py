import random
import time


class AdjacencyMatrixGraph:
    def __init__(self, num_vertices: int, max_edges_per_vertex: int):
        self.num_vertices = num_vertices
        self.max_edges_per_vertex = max_edges_per_vertex
        self.adjacency_matrix = self.generate_adjacency_matrix()

    def generate_adjacency_matrix(self):
        random.seed(time.time())

        # Создаем пустую матрицу смежности
        adjacency_matrix = [[0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
        edge_counts = [0 for _ in range(self.num_vertices)]  # Счетчик ребер для каждой вершины

        for i in range(self.num_vertices):
            # Создаем список вершин, кроме текущей, чтобы избежать ссылки на саму себя
            possible_edges = list(range(self.num_vertices))
            possible_edges.remove(i)
            random.shuffle(possible_edges)

            for edge in possible_edges:
                # Проверяем, существует ли уже ребро или его обратное
                if not (adjacency_matrix[i][edge] or adjacency_matrix[edge][i]):
                    # Проверяем, не превышено ли максимальное количество ребер для обеих вершин
                    if edge_counts[i] < self.max_edges_per_vertex and edge_counts[edge] < self.max_edges_per_vertex:
                        adjacency_matrix[i][edge] = 1
                        adjacency_matrix[edge][i] = 1
                        edge_counts[i] += 1
                        edge_counts[edge] += 1

        return adjacency_matrix

    def print_adjacency_matrix(self):
        for row in self.adjacency_matrix:
            print(row)

    def to_vertex_edge_set(self):
        # Создаем множества для вершин и ребер
        vertices = set(range(self.num_vertices))
        edges = set()

        # Преобразуем матрицу смежности в множество ребер
        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):  # начинаем с i+1, чтобы избежать дубликатов
                if self.adjacency_matrix[i][j] == 1:
                    edges.add((i, j))
        print(f"Рёбра: {vertices}")
        print(f"Вершины: {edges}")
        return vertices, edges

    def to_adjacency_list(self):
        # Создаем пустой список смежности
        adjacency_list = {vertex: [] for vertex in range(self.num_vertices)}

        # Преобразуем матрицу смежности в список смежности
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.adjacency_matrix[i][j] == 1:
                    adjacency_list[i].append(j)

        print(adjacency_list)
        return adjacency_list

gg = AdjacencyMatrixGraph(10, 3)