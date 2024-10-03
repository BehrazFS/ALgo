import heapq
from collections import deque, defaultdict

from unionfind import UnionFind


def bfs_longest_path(graph, start):
    visited = {start}
    queue = deque([(start, 0)])
    max_distance = 0
    farthest_node = start

    while queue:
        node, dist = queue.popleft()
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
                if dist + 1 > max_distance:
                    max_distance = dist + 1
                    farthest_node = neighbor
    return farthest_node, max_distance


def calculate_diameter(graph, mst_nodes):
    if not mst_nodes:
        return 0
    first_node = next(iter(mst_nodes))
    farthest_node, _ = bfs_longest_path(graph, first_node)
    _, diameter = bfs_longest_path(graph, farthest_node)
    return diameter


def farthest_insertion_heuristic_optimized(graph, n, diameter_limit):
    mst = []  # To store the edges of the MST
    mst_nodes = {0}
    uf = UnionFind(n, 1)

    # Priority queue to store potential edges (weight, u, v)
    pq = []
    for v, w in graph[0]:
        heapq.heappush(pq, (w, 0, v))

    mst_graph = defaultdict(list)

    while pq and len(mst) < n - 1:
        weight, u, v = heapq.heappop(pq)
        if v not in mst_nodes:
            mst.append((u, v, weight))  # Store the edge
            mst_nodes.add(v)
            mst_graph[u].append((v, weight))
            mst_graph[v].append((u, weight))
            uf.union(u, v)

            # Update priority queue with new edges
            for w, w_weight in graph[v]:
                if w not in mst_nodes:
                    heapq.heappush(pq, (w_weight, v, w))

            # Calculate the current diameter of the MST
            diameter = calculate_diameter(mst_graph, mst_nodes)
            if diameter > diameter_limit:
                mst.pop()  # Remove the last edge if it exceeds the diameter limit
                mst_nodes.remove(v)
                mst_graph[u].remove((v, weight))
                mst_graph[v].remove((u, weight))
                break

    return mst, diameter


def add_vertex_to_graph(graph, new_vertex):
    n = len(graph)
    graph.append([])
    for i, weight in enumerate(new_vertex):
        graph[i].append((n, weight))


def print_mst(mst):
    print("Minimum Spanning Tree Edges:")
    for edge in mst:
        print(edge)


if __name__ == "__main__":
    graph = [
        [(1, 1), (2, 2), (3, 3)],
        [(0, 1), (2, 4), (3, 5)],
        [(0, 2), (1, 4), (3, 6)],
        [(0, 3), (1, 5), (2, 6)]
    ]

    diameter_limit = 2  # Number of edges

    mst_edges, max_diameter = farthest_insertion_heuristic_optimized(graph, len(graph), diameter_limit)
    print_mst(mst_edges)
    print(f"Maximum Diameter of MST: {max_diameter}")

    new_vertex = [7, 8, 9, 10]

    add_vertex_to_graph(graph, new_vertex)

    mst_edges, max_diameter = farthest_insertion_heuristic_optimized(graph, len(graph), diameter_limit)
    print("\nAfter adding new vertex:")
    print_mst(mst_edges)
    print(f"Maximum Diameter of MST: {max_diameter}")
