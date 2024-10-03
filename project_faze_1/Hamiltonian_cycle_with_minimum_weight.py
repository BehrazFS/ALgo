def tsp(graph):
    """
    just some information :
    Finding a Hamiltonian cycle with minimum weight in a directed graph is a classic NP-hard problem known as the
    "Traveling Salesman Problem" (TSP) in the case of symmetric graphs and the "Asymmetric Traveling Salesman
    Problem" (ATSP) in the case of directed graphs.
    """
    n = len(graph)
    dp = [[float('inf')] * n for _ in range(1 << n)]  # dp[mask][u] : with mask as bitwise visited min path from 0 to u
    parent = [[-1] * n for _ in range(1 << n)]
    dp[1][0] = 0  # start at node 0 for dp
    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if not mask & (1 << v) and graph[u][v] != float('inf'):
                        new_mask = mask | (1 << v)
                        if dp[new_mask][v] > dp[mask][u] + graph[u][v]:
                            dp[new_mask][v] = dp[mask][u] + graph[u][v]
                            parent[new_mask][v] = u
    min_cost = float('inf')
    last_node = -1
    final_mask = (1 << n) - 1
    for v in range(1, n):
        if dp[final_mask][v] + graph[v][0] < min_cost:
            min_cost = dp[final_mask][v] + graph[v][0]
            last_node = v
    if min_cost == float('inf'):
        return None, float('inf')

    path = []
    mask = final_mask
    node = last_node
    while node != -1:
        path.append(node)
        next_node = parent[mask][node]
        mask ^= (1 << node)
        node = next_node

    path.reverse()

    path.append(0)
    return path, min_cost


def build(graph):
    g = [[float('inf')] * len(graph[0]) for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if i != j:
                g[i][j] = graph[i][j]
    return g


if __name__ == "__main__":
    graph = [
        [float('inf'), 10, 15, 20],
        [10, float('inf'), 35, 25],
        [15, 35, float('inf'), 30],
        [20, 205, 30, float('inf')]
    ]
    path, min_cost = tsp(graph)
    if path is None:
        print("No Hamiltonian cycle found.")
    else:
        print(f"The minimum weight Hamiltonian cycle is {path} with cost {min_cost}.")
