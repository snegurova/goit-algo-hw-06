"""Module providing graph searches."""
import networkx as nx

from graph import G
def dfs(graph, start):
    """Function implementing depth first search"""
    visited = set()
    stack = [start]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(set(graph[vertex]) - visited)

    return path

def bfs(graph, start):
    """Function implementing breadth first search"""
    visited = set()
    queue = [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(set(graph[vertex]) - visited)

    return path

graph_dict = nx.to_dict_of_lists(G)
start_node = 'Dnipro'
dfs_path = dfs(graph_dict, start_node)
bfs_path = bfs(graph_dict, start_node)

print(f"DFS path starting from {start_node}: {dfs_path}")
print(f"BFS path starting from {start_node}: {bfs_path}")
