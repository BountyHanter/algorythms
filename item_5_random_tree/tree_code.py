import random, time

random.seed(time.time())
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_children(self, level, probabilities):
        num_children = random.choices(list(probabilities.keys()), weights=probabilities.values(), k=1)[0]
        self.children.extend(Node(f'Child {level+1}.{i+1}') for i in range(num_children))


def build_tree(root, depth, probabilities, level=0):
    if depth > 0:
        root.add_children(level, probabilities)
        for child in root.children:
            build_tree(child, depth-1, probabilities, level+1)


def display_tree(node, level=0, all = []):
    print('  ' * level + node.value)
    all.append(node.value)
    for child in node.children:
        display_tree(child, level+1)
    return all


from collections import defaultdict

def count_nodes_per_level(node, level=0, counts=None):
    if counts is None:
        counts = defaultdict(int)
    counts[level] += 1
    for child in node.children:
        count_nodes_per_level(child, level+1, counts)
    return counts

if __name__ == "__main__":


    # Пример использования
    probabilities = {1: 1, 2: 1/2, 3: 1/4, 5: 1/10}
    root = Node('Root')
    build_tree(root, 3, probabilities)
    display_tree(root)
    print(root.value)
    node_counts = count_nodes_per_level(root)
    for level, count in node_counts.items():
        print(f'Уровень {level}: {count} узлов')

    """
    
    # Пример использования
    #probabilities = {1: 1, 2: 1/2, 3: 1/4, 5: 1/100}
    #root = Node('Root')
    #build_tree(root, 3, probabilities)
    #display_tree(root)
    
    def count_nodes(node):
        return 1 + sum(count_nodes(child) for child in node.children)
    
    # Пример использования
    #num_nodes = count_nodes(root)
    #print(f'Количество узлов: {num_nodes}')
    
    
    def count():
        probabilities = {1: 1, 2: 1 / 2, 3: 1 / 4, 5: 1 / 10}
        root = Node('Root')
        build_tree(root, 3, probabilities)
        num_nodes = count_nodes(root)
        return num_nodes
    full = 0
    for i in range(1,10001):
        gg = count()
        full += gg
    print(full/10000)
    """