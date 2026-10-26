from heapq import heappush, heappop

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            target = state[i] - 1
            distance += abs(i // 3 - target // 3)
            distance += abs(i % 3 - target % 3)
    return distance

def solve(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, [start]))
    best_cost = {start: 0}

    while pq:
        f, g, state, path = heappop(pq)

        if state == goal:
            for s in path:
                for i in range(0, 9, 3):
                    print(s[i:i+3])
                print()
            print("Moves:", len(path) - 1)
            return

        if g != best_cost[state]:
            continue

        blank = state.index(0)
        r, c = divmod(blank, 3)

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                nb = nr * 3 + nc
                new = list(state)
                new[blank], new[nb] = new[nb], new[blank]
                new = tuple(new)
                new_g = g + 1

                if new_g < best_cost.get(new, float('inf')):
                    best_cost[new] = new_g
                    heappush(pq, (
                        new_g + heuristic(new),
                        new_g,
                        new,
                        path + [new]
                    ))

    print("No solution found")

start = tuple(map(int, input("Enter 9 numbers (0 for blank): ").split()))
solve(start)