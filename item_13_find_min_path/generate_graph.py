import networkx as nx
import matplotlib.pyplot as plt
import random


# Ваша функция для генерации графа
def generate_weighted_directed_graph(num_vertices, edge_probability=0.3, max_weight=10):
    graph = {i: [] for i in range(1, num_vertices + 1)}
    for i in range(1, num_vertices + 1):
        for j in range(1, num_vertices + 1):
            if i != j and random.random() < edge_probability:
                weight = random.randint(1, max_weight)
                graph[i].append((j, weight))
    return graph


if __name__ == "__main__":

    # Генерация графа
    num_vertices = 10  # Количество вершин
    graph = generate_weighted_directed_graph(num_vertices)

    # Создание ориентированного графа в NetworkX
    G = nx.DiGraph()
    for node in graph:
        G.add_node(node)
        for edge in graph[node]:
            G.add_edge(node, edge[0], weight=edge[1])

    # Рисование графа
    pos = nx.spring_layout(G)  # Расположение вершин графа
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15,
            arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    plt.show()  # Показать граф
