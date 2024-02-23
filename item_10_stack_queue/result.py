"""
Стек нужен когда важен порядок LIFO - в основном для Обработки рекурсий
Очередь нужна когда важен FIFO - Обработка задач в ОС, алгоритм обхода в ширину (для отслеживания вершин которые
следует посетить), симуляция реального мира

Преимущества связного списка - Динамический размер, затраты по памяти, эффективны при удалении и добавлени так как
нужно просто поиграть с указателями
Статический массив - ограниченный размер, быстрый доступ к данным так как хранится в виде непрерывнгго блока памяти,
не эффективны при удалении и вставке так как нужно перемещать все элементы
"""

class Stack:
    def __init__(self, size):
        self.stack = [None] * size # сразу выделяем память под стек
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def push(self, item):
        if self.top == len(self.stack) - 1:
            raise Exception("Стек переполнен")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            raise Exception("Стек пуст")
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def contains(self, item):
        return item in self.stack

    def print_stack(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])

    def peek(self):
        if self.is_empty():
            raise Exception("Стек пуст")
        return self.stack[self.top]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Стек пуст")
        data = self.top.data
        self.top = self.top.next
        return data

    def contains(self, item): # Поиск элемента
        current = self.top
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.data)
            current = current.next

    def peek(self):
        if self.is_empty():
            raise Exception("Стек пуст")
        return self.top.data


class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.head = 0
        self.tail = 0
        self.size = size

    def is_empty(self):
        return self.head == self.tail and self.queue[self.head] is None

    def is_full(self):
        return self.head == self.tail and self.queue[self.head] is not None

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Очередь переполнена")
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            raise Exception("Очередь пуста")
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.size
        return item

    def contains(self, item):
        return item in self.queue

    def print_queue(self):
        i = self.head
        while i != self.tail:
            print(self.queue[i])
            i = (i + 1) % self.size


class Node1:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue1:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node1(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Очередь пуста")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def take_first(self):
        if self.is_empty():
            return None
        return self.head

    def contains(self, item):
        """ Check if item in queue"""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def print_queue(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

if __name__ == '__main__':
    gg = Stack(10)
    gg.push(1)
    gg.push(2)
    gg.push(3)
    print(gg.peek())

    stack = [None]*5
    print(stack)