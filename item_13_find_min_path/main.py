from generate_graph import generate_weighted_directed_graph

result = generate_weighted_directed_graph(10)
print(result)

res = {}
# Убираю веса
for i in result:
    for b in enumerate(result[i]):
        gg = b[0]
        result[i][gg] = result[i][gg][0]
print(result)


def find_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        print(path)  # или возвращаем path
        return
    for next_vertex in graph[start]:
        if next_vertex not in path:  # Избегаем циклов
            find_paths(graph, next_vertex, end, path)


find_paths(result, 3, 10)

