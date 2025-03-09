import matplotlib.pyplot as plt
import networkx as nx

def visualize_flight_path(graph, path):
    """Visualize the optimized flight path."""
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=300, node_color='lightblue')
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)
    plt.show()
