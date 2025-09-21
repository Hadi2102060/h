from collections import deque

def bfs(tree, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited: 
            print(node, end="")
            visited.append(node)

            for neighbor in tree[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


tree = {
    'A': ['B', 'E'],
    'B': ['c', 'D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs(tree, 'A')