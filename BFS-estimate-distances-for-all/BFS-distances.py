

import sys


col0 = [-1,  3,  2, -1]
col1 = [-1, -1,  5,  2]
col2 = [-1, -1, -1,  3]
col3 = [-1, -1, -1, -1]


graph = [col0, col1, col2, col3]


def getpathsbfs(graph, start):
    queue = []
    queue.append([start])
    visited = [-1] * len(graph)
    path = []
    d = [sys.maxsize] * len(graph)
    queue = [start]
    d[0] = 0
    while queue:
        currentnode = queue.pop(0)
        path.append(currentnode)
        for neighbornode in range(len(graph)):
            if graph[currentnode][neighbornode] > 0:
                if visited[neighbornode] == -1:
                    visited[neighbornode] = 0
                    new_path = list(path)
                    new_path.append(neighbornode)
                    d[neighbornode] = d[currentnode]+1
                    queue.append(neighbornode)
            visited[currentnode] = 1
    return d


print(getpathsbfs(graph, 0))
