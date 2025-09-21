def dfs(tree, start , visited = []):
    if start not in visited:
        print(start, end=" ")
        visited.append(start)

        for node in tree[start]:
            dfs(tree, node, visited)


tree = {
    'A': ['B', 'E'],
    'B': ['C', 'D'],    
    'C': ['F'],
    'D': [],    
    'E': [],
    'F': []
}

dfs (tree, "A")