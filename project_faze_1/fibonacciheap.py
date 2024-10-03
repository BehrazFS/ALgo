import math


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.degree = 0
        self.marked = False
        self.parent = None
        self.child = None
        self.left = self
        self.right = self

    def __str__(self):
        return f"({self.value!s},{self.key!s})"

    def __repr__(self):
        return str(self)


class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.total_nodes = 0

    def insert(self, key, value):
        node = Node(key, value)
        self._add_node(node)
        if not self.min or node.key < self.min.key:
            self.min = node
        self.total_nodes += 1
        return node

    def _add_node(self, node):
        if self.min is None:
            self.min = node
        else:
            node.left = self.min
            node.right = self.min.right
            self.min.right = node
            node.right.left = node

    def extract_min(self):
        z = self.min
        if z:
            if z.child:
                children = [x for x in self._iterate(z.child)]
                for child in children:
                    self._add_node(child)
                    child.parent = None

            self._remove_node(z)
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self._consolidate()

            self.total_nodes -= 1
        return z

    @staticmethod
    def _remove_node(node):
        node.left.right = node.right
        node.right.left = node.left

    def _consolidate(self):
        array_size = int(math.log(self.total_nodes) * 2)
        A = [None] * array_size

        nodes = [x for x in self._iterate(self.min)]
        for w in nodes:
            x = w
            d = x.degree
            while A[d]:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self._link(y, x)
                A[d] = None
                d += 1
            A[d] = x

        self.min = None
        for i in range(array_size):
            if A[i]:
                if not self.min or A[i].key < self.min.key:
                    self.min = A[i]

    def _link(self, y, x):
        self._remove_node(y)
        y.parent = x
        if not x.child:
            x.child = y
            y.right = y
            y.left = y
        else:
            y.left = x.child
            y.right = x.child.right
            x.child.right = y
            y.right.left = y
        x.degree += 1
        y.marked = False

    def decrease_key(self, x, k):
        if k > x.key:
            raise ValueError("new key is greater than current key")
        x.key = k
        y = x.parent
        if y and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)
        if x.key < self.min.key:
            self.min = x

    def _cut(self, x, y):
        self._remove_node(x)
        y.degree -= 1
        if x == x.right:
            y.child = None
        else:
            y.child = x.right
        x.parent = None
        x.left = x.right = x
        self._add_node(x)
        x.marked = False

    def _cascading_cut(self, y):
        z = y.parent
        if z:
            if not y.marked:
                y.marked = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def delete(self, x):
        self.decrease_key(x, float('-inf'))
        self.extract_min()

    @staticmethod
    def _iterate(head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right
