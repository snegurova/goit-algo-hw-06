"""Module providing a function implementing dejkstra algorithm"""
import heapq

import networkx as nx
import matplotlib.pyplot as plt

from graph import G

# Додавання ваг до ребер
weighted_edges = [('Dnipro', 'Kyiv', 477), ('Dnipro', 'IFrankivsk', 943), ('Kyiv', 'Lviv', 561), \
                  ('IFrankivsk', 'Lviv', 133), ('IFrankivsk', 'Ternopil', 132), \
                    ('Lviv', 'Ternopil', 127), ('Ternopil', 'Vinnycia', 234)]
G.clear()
G.add_weighted_edges_from(weighted_edges)

# Візуалізація графа з вагами
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Weighted Transport Network')
plt.show()

def dijkstra(graph, start):
    """Function implementing dejkstra algorithm"""
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    path = {node: None for node in graph.nodes}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, path

start_node = 'Dnipro'
distances, paths = dijkstra(G, start_node)

print(f"Shortest distances from {start_node}: {distances}")
print(f"Paths: {paths}")
