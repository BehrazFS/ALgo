from fibonacciheap import FibonacciHeap
from unionfind import UnionFind


class Graph:
    def __init__(self, vertices, adj_matrix):
        self.V = vertices
        self.edges = []
        self.adj_list = [[] for _ in range(self.V)]
        self.adj_matrix = adj_matrix
    @staticmethod
    def build_graph(edges, n):
        adj_list = [[] for _ in range(n)]
        for u, v, w in edges:
            adj_list[u].append([v, w])
        return adj_list

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])
        self.adj_list[u].append([v, w])

    def kruskal_mst(self, edges):
        mst_tree = []
        i, number_of_edges = 0, 0
        edges = sorted(edges, key=lambda item: item[2])
        union = UnionFind(self.V, 0)
        while number_of_edges < self.V - 1:
            u, v, w = edges[i]
            i = i + 1
            x = union.find(u)
            y = union.find(v)
            if x != y:
                number_of_edges = number_of_edges + 1
                mst_tree.append([u, v, w])
                union.union(x, y)
        return mst_tree

    def prim_mst(self):
        fib_heap = FibonacciHeap()
        mst_set = [False] * self.V
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        heap_nodes = [None] * self.V
        for v in range(self.V):
            if v == 0:
                heap_nodes[v] = fib_heap.insert(0, v)
                key[v] = 0
            else:
                heap_nodes[v] = fib_heap.insert(float('inf'), v)
        while fib_heap.total_nodes > 0:
            min_node = fib_heap.extract_min()
            u = min_node.value
            mst_set[u] = True
            for neighbor, weight in self.adj_list[u]:
                if not mst_set[neighbor] and key[neighbor] > weight:
                    key[neighbor] = weight
                    parent[neighbor] = u
                    fib_heap.decrease_key(heap_nodes[neighbor], weight)
        mst_edges = []
        total_weight = 0
        for v in range(1, self.V):
            if parent[v] != -1:
                mst_edges.append([parent[v], v, key[v]])
                total_weight += key[v]

        return mst_edges  # , total_weight

    def add_vertex_to_graph(self, new_vertex):
        n = self.V
        new_edges = []
        self.adj_matrix.append(new_vertex + [0])
        self.adj_list.append([])
        for i in range(self.V):
            self.adj_matrix[i] += [new_vertex[i]]
            self.adj_list[i].append([n, new_vertex[i]])
            self.adj_list[n].append([i, new_vertex[i]])
        for i, weight in enumerate(new_vertex):
            self.edges.append([n, i, weight])
            self.edges.append([i, n, weight])
            new_edges.append([n, i, weight])
            new_edges.append([i, n, weight])
        self.V += 1
        return new_edges


if __name__ == '__main__':
    num_vertices = 5
    costs = [
        [0, 2, 3, 1, 4],
        [2, 0, 2, 3, 3],
        [3, 2, 0, 4, 2],
        [1, 3, 4, 0, 5],
        [4, 3, 2, 5, 0]
    ]
    g = Graph(num_vertices, costs)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j:
                g.add_edge(i, j, costs[i][j])
    from experimental import print_mst

    print_mst(g.prim_mst())
    g.add_vertex_to_graph([1, 2, 3, 4, 5])
    print(g.adj_list)
    print(g.edges)
    print(g.adj_matrix)
    print_mst(g.prim_mst())
