import random

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Generate a random degree distribution
np.random.seed(42)
degree_sequence = np.random.zipf(a=2, size=300)
degree_sequence = np.clip(degree_sequence, 1, 50)  # Limit degrees

# Ensure the sum of degrees is even
if sum(degree_sequence) % 2 != 0:
    degree_sequence[0] += 1  # Adjust to make sum even

# Create a network with the given degree distribution
G_random_degree = nx.configuration_model(degree_sequence)
G_random_degree = nx.Graph(G_random_degree)  # Remove loops and parallel edges
G_random_degree.remove_edges_from(nx.selfloop_edges(G_random_degree))

def rewire_graph(G, p=0.1):
    """
    Randomly rewires the edges of a graph with a given probability.
    
    :param G: Input graph
    :param p: Probability of edge rewiring
    :return: Modified graph with rewired edges
    """
    G_rewired = G.copy()
    edges = list(G_rewired.edges())
    nodes = list(G_rewired.nodes())

    for u, v in edges:
        if random.random() < p:  # Probability of edge rewiring
            G_rewired.remove_edge(u, v)
            new_v = random.choice(nodes)
            while new_v == u or G_rewired.has_edge(u, new_v):
                new_v = random.choice(nodes)
            G_rewired.add_edge(u, new_v)

    return G_rewired

# Create and visualize 4 rewired networks using the rewiring technique
rewired_graphs = [rewire_graph(G_random_degree, p=0.1) for _ in range(4)]

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
axes = axes.flatten()
for i, G_rewired in enumerate(rewired_graphs):
    ax = axes[i]
    nx.draw(G_rewired, node_size=30, edge_color="gray", alpha=0.6, ax=ax)
    ax.set_title(f"Rewired Network {i+1}")

plt.show()
