graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

# def dfs(graph, start):
#     visited, stack = set(), [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             stack.extend(graph[vertex] - visited)
#     return visited

def dfs(graph, start, visited):
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

def dfs_driver(graph, start):
    visited = set()
    return dfs(graph, start, visited)

print dfs_driver(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}