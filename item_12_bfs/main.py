from item_5_random_tree.tree_code import display_tree, Node, build_tree
from item_10_stack_queue.result import Queue1

probabilities = {1: 1, 2: 1/2, 3: 1/4, 5: 1/10}
root = Node('Root')
build_tree(root, 3, probabilities)
display_tree(root)


def take_all(root: root):
    my_queue = Queue1()
    root.children
