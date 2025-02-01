import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def create_social_network(n_clusters=4, cluster_size=75, p_in=0.1, p_out=0.01):
    """
    Creates a clustered social network where intra-cluster connections are stronger than inter-cluster connections.
    
    :param n_clusters: Number of clusters
    :param cluster_size: Number of nodes per cluster
    :param p_in: Probability of intra-cluster edge creation
    :param p_out: Probability of inter-cluster edge creation
    :return: A generated social network graph
    """
    G = nx.Graph()
    clusters = []
    
    for i in range(n_clusters):
        # Generate nodes for each cluster
        nodes = range(i * cluster_size, (i + 1) * cluster_size)
        G.add_nodes_from(nodes)
        clusters.append(set(nodes))
        
        # Create intra-cluster connections
        for u in nodes:
            for v in nodes:
                if u < v and np.random.rand() < p_in:
                    G.add_edge(u, v)
                    
    # Create inter-cluster connections
    for i in range(n_clusters):
        for j in range(i + 1, n_clusters):
            for u in clusters[i]:
                for v in clusters[j]:
                    if np.random.rand() < p_out:
                        G.add_edge(u, v)

    return G

# Generate and visualize the social network
g_social = create_social_network()
plt.figure(figsize=(8, 6))
nx.draw(g_social, node_size=30, edge_color="gray", alpha=0.6)
plt.title("Social Network with Girvan-Newman Structure")
plt.show()
