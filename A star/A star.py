
graph = {
    'S': {'A': 1, 'G': 10, },
    'A': {'B': 2, 'C': 1},
    'B': {'D': 5},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 2 }
}

h = {'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G':0}

def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]
    best_cost = {start: 0}

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if g != best_cost[node]:
            continue

        if node == goal:
            print("Path:", path)
            print("Total cost:", g)
            return

        for child, cost in graph[node].items():
            new_g = g + cost

            if new_g < best_cost.get(child, float('inf')):
                best_cost[child] = new_g
                new_f = new_g + h[child]
                open_list.append(
                    (new_f, new_g, child, path + [child])
                )

    print("Goal not found")

start = input("Enter start node (S-G): ").upper()
goal = input("Enter goal node (S-G): ").upper()

astar(start, goal)
