def prims_min(graph, n):
    visited = [False] * n
    visited[0] = True

    total_cost = 0
    print("\nEdges in Minimum Spanning Tree:")

    for count in range(n - 1):
        minimum = float('inf')
        x = y = 0

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(x, "--", y, "=", minimum)
        total_cost += minimum
        visited[y] = True

    print("Minimum Cost =", total_cost)


def prims_max(graph, n):
    visited = [False] * n
    visited[0] = True

    total_cost = 0
    print("\nEdges in Maximum Spanning Tree:")

    for count in range(n - 1):
        maximum = float('-inf')
        x = y = 0

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j] != 0:
                        if graph[i][j] > maximum:
                            maximum = graph[i][j]
                            x = i
                            y = j

        print(x, "--", y, "=", maximum)
        total_cost += maximum
        visited[y] = True

    print("Maximum Cost =", total_cost)


# Graph
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

n = 5

# Minimum Spanning Tree
prims_min(graph, n)

# Maximum Spanning Tree
prims_max(graph, n)
