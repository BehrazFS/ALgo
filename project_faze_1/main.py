from graph import Graph
from experimental import farthest_insertion_heuristic_optimized, print_mst
from Hamiltonian_cycle_with_minimum_weight import tsp, build

print("menu : ")
num_vertices = int(input("initial size : "))
costs = []
current_mst = []
print("input adjacency matrix : \n")
for i in range(num_vertices):
    costs.append(list(map(int, input().split())))
# print(costs)
g = Graph(num_vertices, costs)
for i in range(num_vertices):
    for j in range(num_vertices):
        if i != j:
            g.add_edge(i, j, costs[i][j])
current_mst = g.prim_mst()  # O(|E| + |V|log|V|)
while True:
    ch = input(
        "menu :\n\tHamiltonian cycle with minimum weight[hcwmw]\n\texit[exit]\n\tmst[mst]\n\tnew vertex["
        "nv]\n\texperimental(might work incorrectly) mst with bound x(x:number) [mwb:x]\n choice : ")
    if ch == "mst":
        print_mst(current_mst)
    elif ch == "nv":
        new_edges = g.add_vertex_to_graph(list(map(int, input().split())))  # O(|V|)
        current_mst = g.kruskal_mst(new_edges + current_mst)  # O(|E|log|E|) and |E| = 2|V|
        print_mst(current_mst)
    elif ch == "exit":
        break
    elif ch == "hcwmw":
        gg = build(g.adj_matrix)
        path, min_cost = tsp(gg)  # O(n^2 * 2^n)
        if path is None:
            print("No Hamiltonian cycle found.")
        else:
            print(f"The minimum weight Hamiltonian cycle is {path} with cost {min_cost}.")

    else:
        ch = ch.split(":")
        if ch[0] == "mwb":
            bound = int(ch[1])
            mst_edges, max_diameter = farthest_insertion_heuristic_optimized(g.adj_list, len(g.adj_list),
                                                                             diameter_limit=bound)  # O(|v|(|V|+|E|))
            print_mst(mst_edges)
            print(f"Maximum Diameter of MST: {max_diameter}")
