def dfs_limited(tree, start, limit, visited=[]):
    if limit <= 0:
        return
    if start not in visited:
        print(start, end=" ")
        visited.append(start)
    for node in tree[start]:
        dfs_limited(tree, node, limit - 1, visited)


def iterative_deepening_dfs(tree, start, max_limit):
    for i in range(max_limit):
        print(f"Iteration {i+1} : ", end=" ")
        dfs_limited(tree, start, i+1, [])
        print()


# graph definition
n = int(input("Enter number of nodes: "))

tree = {}
for i in range(n):
    node = input(f"Enter node name ({i+1}): ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    tree[node] = neighbors

start = input("Enter start node: ")
max_limit = int(input("Enter maximum depth limit: "))

# run IDDFS
iterative_deepening_dfs(tree, start, max_limit)