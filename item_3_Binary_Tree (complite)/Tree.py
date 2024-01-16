


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def insert(self, value):
        """Вставка элемента в бинарное дерево"""
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        """Рекурсивный метод для вставки элемента"""
        if value < current.value:
            if current.left:
                self._insert_recursive(current.left, value)
            else:
                current.left = TreeNode(value)
        else:
            if current.right:
                self._insert_recursive(current.right, value)
            else:
                current.right = TreeNode(value)

    def search(self, value):
        """Поиск элемента в бинарном дереве"""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        """Рекурсивный метод для поиска элемента"""
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

    def max_depth(self):
        """Вычисление максимальной глубины бинарного дерева"""
        return self._max_depth_recursive(self.root)

    def _max_depth_recursive(self, current):
        """Рекурсивный метод для вычисления максимальной глубины"""
        if current is None:
            return 0
        left_depth = self._max_depth_recursive(current.left)
        right_depth = self._max_depth_recursive(current.right)
        return max(left_depth, right_depth) + 1

    def print_tree_values(self):
        """Отображение всех элементов дерева"""
        self._print_tree_values_recursive(self.root)

    def _print_tree_values_recursive(self, current):
        """Рекурсивный метод для отображения элементов дерева"""
        if current is None:
            return

        self._print_tree_values_recursive(current.left)
        print(current.value)
        self._print_tree_values_recursive(current.right)

"""
# Проба
tree = BinaryTree()
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)
tree.insert(22)

print("Поиск элемента 7:", tree.search(7))
print("Поиск элемента 9:", tree.search(9))
print("Максимальная глубина дерева:", tree.max_depth())
"""



