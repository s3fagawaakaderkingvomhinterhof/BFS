

col0 = [-1, 3, 2, -1]
col1 = [0, -1, 5, 2]
col2 = [0, 0, -1, 3]
col3 = [-1, 0, 0, -1]


graph = [col0, col1, col2, col3]


paths_all = []


def getpathsbfs(graph, start, end):
	nodes = len(graph)
    queue = []
    queue.append([start])
    visited = [-1] * nodes
    while queue:
        path = queue.pop(0)
        currentnode = path[-1]
        visited[currentnode] = 1
        if currentnode == end:
            paths_all.append(path)
        for neighbor in range(len(graph)):
            if graph[currentnode][neighbor] > 0:
                if visited[currentnode] == 1:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
    return paths_all


 print(getpathsbfs(graph, 0, 3))