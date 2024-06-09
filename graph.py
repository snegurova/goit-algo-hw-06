"""Module providing graph creating, analyzing and visualization."""
import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (наприклад, зупинки транспорту)
nodes = ['Dnipro', 'Kyiv', 'IFrankivsk', 'Lviv', 'Ternopil', 'Vinnycia']
G.add_nodes_from(nodes)

# Додавання ребер (наприклад, транспортні маршрути)
edges = [('Dnipro', 'Kyiv'), ('Dnipro', 'IFrankivsk'), ('Kyiv', 'Lviv'), ('IFrankivsk', 'Lviv'), \
         ('IFrankivsk', 'Ternopil'), ('Lviv', 'Ternopil'), ('Ternopil', 'Vinnycia')]
G.add_edges_from(edges)

if __name__ == "__main__":
    # Візуалізація графа
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  # Позиції вершин для кращої візуалізації
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
    plt.title('Transport Network')
    plt.show()

    # Аналіз характеристик графа
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degree_sequence = dict(G.degree())

    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print("Degree of each node:", degree_sequence)
