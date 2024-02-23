from item_5_random_tree.tree_code import display_tree, Node, build_tree
from item_10_stack_queue.result import Queue1

probabilities = {1: 1, 2: 1/2, 3: 1/4, 5: 1/10}
root = Node('Root')
build_tree(root, 3, probabilities)
display_tree(root)

my_queue = Queue1()
element = (root.value, root.children)
my_queue.enqueue(element)
#print(my_queue.take_first().data)
while True:
    first_element = my_queue.take_first()
    if first_element is not None:
        element = (first_element.data[0], first_element.data[1])
        for child in element[1]:
            if child is not None: # Чтобы не обрабатывать пустые дочерние элементы
                new_element = (child.value, child.children)
                #print(new_element)
                my_queue.enqueue(new_element)
        my_queue.print_queue()
        print('Конец очереди')
        my_queue.dequeue()
        continue
    else:
        break




def take_all(root: root):
    pass
