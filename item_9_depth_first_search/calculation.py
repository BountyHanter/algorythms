import networkx as nx
import matplotlib.pyplot as plt
import time

def create_graph(n):
    m = n
    graph = {}
    for i in range(n):
        for j in range(m):
            node = i * m + j
            if node not in graph:
                graph[node] = []
            if j < m - 1:
                graph[node].append(node + 1)
            else:
                graph[node].append(i * m)  # замыкаем цикл
    return graph

def count_components(graph):
    """
    Сложность = O(V+E), где V - количество рёбер, Е - количество вершин
    """
    visited = set()
    count = 0

    def dfs(node):
        nonlocal visited
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1

    return count

def draw_graph(graph):
    G = nx.Graph()
    for node, edges in graph.items():
        for edge in edges:
            G.add_edge(node, edge)

    nx.draw(G, with_labels=True)
    plt.show()


lst = [i for i in range(100,1000,100)]
result = {}

for i in lst:
    graph = create_graph(i)
    start_time = time.time()
    count_components(graph)
    end_time = time.time()
    res = end_time-start_time
    print(res)
    result[i] = res
print(result)

plt.figure(figsize=(8, 5))
plt.plot(list(result.keys()), list(result.values()), marker='o', linestyle='-', color='m')
plt.title('Отношение времени поиска ребра к n')
plt.xlabel('Количество рёбер')
plt.ylabel('Время(сек.)')
plt.grid(True)

plt.show()