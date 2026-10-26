
graph = {
    'A': ['B', 'D'],
    'B': ['E', 'C'],
    'D': ['E', 'G'],
    'E': ['H'],
    'C': ['F'],
    'E': [],
    'G': []
}

def dls(node, goal, depth):
    print(node, end=" ")

    if node == goal:
        return True

    if depth == 0:
        return False

    for child in graph[node]:
        if dls(child, goal, depth - 1):
            return True

    return False

start = 'A'
goal = 'G'

for limit in range(len(graph)):
    print("\nDepth limit:", limit)

    if dls(start, goal, limit):
        print("\nGoal found!")
        break
else:
    print("\nGoal not found!")
