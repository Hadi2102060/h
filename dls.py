def dls(tree, start, limit, visited = []):
    if limit <=0:
        return
    if start not in visited:
        print(start, end=" ")
        visited.append(start)
    for node in tree[start]:
        dls(tree, node, limit-1, visited)


tree ={
    'A': ['B', 'E'],
    'B': ['C', 'D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F':[]
}

dls(tree, 'A', 3)