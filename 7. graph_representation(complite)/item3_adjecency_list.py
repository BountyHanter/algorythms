import random


class AdjacencyListGraph:
    def __init__(self, num_vertices: int, max_edges_per_vertex: int):
        self.num_vertices = num_vertices
        self.max_edges_per_vertex = max_edges_per_vertex
        self.adjacency_list = self.generate_adjacency_list()

    def generate_adjacency_list(self):
        # Создаем пустой список смежности
        adjacency_list = {vertex: [] for vertex in range(self.num_vertices)}
        edge_counts = [0 for _ in range(self.num_vertices)]  # Счетчик ребер для каждой вершины

        for i in range(self.num_vertices):
            # Создаем список вершин, кроме текущей, чтобы избежать ссылки на саму себя
            possible_edges = list(range(self.num_vertices))
            possible_edges.remove(i)

            random.shuffle(possible_edges)

            for edge in possible_edges:
                # Проверяем, существует ли уже ребро или его обратное
                if edge not in adjacency_list[i] and i not in adjacency_list[edge]:
                    # Проверяем, не превышено ли максимальное количество ребер для обеих вершин
                    if edge_counts[i] < self.max_edges_per_vertex and edge_counts[edge] < self.max_edges_per_vertex:
                        adjacency_list[i].append(edge)
                        adjacency_list[edge].append(i)
                        edge_counts[i] += 1
                        edge_counts[edge] += 1

        return adjacency_list

    def print_adjacency_list(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")

    def count_edges(self):
        edge_count = 0
        for edges in self.adjacency_list.values():
            edge_count += len(edges)
        return edge_count//2 # так как каждое ребро учитывается дважды

    def edge_exists(self, edge):
        return edge[1] in self.adjacency_list[edge[0]]

    def to_vertex_edge_set(self):
        # Создаем множества для вершин и ребер
        vertices = set(range(self.num_vertices))
        edges = set()

        # Преобразуем список смежности в множество ребер
        for vertex, connected_vertices in self.adjacency_list.items():
            for connected_vertex in connected_vertices:
                # Добавляем ребро в множество ребер, если его там еще нет
                if (connected_vertex, vertex) not in edges:
                    edges.add((vertex, connected_vertex))

        print(f"Вершины: {vertices}\nРёбра:{edges}")
        return vertices, edges

    def to_adjacency_matrix(self):
        # Создаем пустую матрицу смежности
        adjacency_matrix = [[0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]

        # Преобразуем список смежности в матрицу смежности
        for vertex, connected_vertices in self.adjacency_list.items():
            for connected_vertex in connected_vertices:
                adjacency_matrix[vertex][connected_vertex] = 1

        for row in adjacency_matrix:
            print(row)
        return adjacency_matrix
