import networkx as nx
import matplotlib.pyplot as plt
import time


def create_disjoint_graph(n):
    graph = {}

    for component in range(n):
        parent = component * n  # Устанавливаем первую вершину компоненты как родительскую

        for i in range(component * n, (component + 1) * n):
            graph[i] = []

            # Создаем связи внутри каждой связной компоненты в виде дерева
            if i > parent:
                graph[parent].append(i)
                graph[i].append(parent)

    return graph



def count_components(graph):

    visited = set()
    components = 0

    def dfs(vertex):
        visited.add(vertex)  # Добавляем текущую вершину в посещенные
        for neighbor in graph[vertex]:  # Обходим всех соседей текущей вершины
            if neighbor not in visited:  # Если соседняя вершина еще не была посещена
                dfs(neighbor)  # Продолжаем обход из соседней вершины

    for vertex in graph:  # Обходим все вершины графа
        if vertex not in visited:
            dfs(vertex)  # Начинаем обход из этой вершины
            components += 1

    return components

def draw_graph(graph):
    G = nx.Graph()
    for node, edges in graph.items():
        for edge in edges:
            G.add_edge(node, edge)

    nx.draw(G, with_labels=True)
    plt.show()


g = create_disjoint_graph(5)
draw_graph(g)
print(count_components(g))