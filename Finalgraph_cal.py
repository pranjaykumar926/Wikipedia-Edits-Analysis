import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
filtered_df = pd.read_csv('source_tgt_val_modified.csv')
G = nx.from_pandas_edgelist(filtered_df, 'Source', 'Target', ['Weight'], create_using=nx.DiGraph())
plt.figure(figsize=(10, 8))
pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos, with_labels=True, node_size=200, font_size=8, alpha=0.8, node_color='skyblue', edge_color='gray')
plt.title('Graph')
plt.show()
degree_distribution = dict(G.degree())
plt.figure(figsize=(8, 6))
plt.bar(degree_distribution.keys(), degree_distribution.values(), color='skyblue')
plt.xlabel('Node')
plt.ylabel('Degree')
plt.title('Degree Distribution')
plt.show()
centrality_measures = {
    'Degree Centrality': nx.degree_centrality(G),
    'Betweenness Centrality': nx.betweenness_centrality(G),
    'Closeness Centrality': nx.closeness_centrality(G),
    'Eigenvector Centrality': nx.eigenvector_centrality(G)
}

plt.figure(figsize=(10, 8))
for measure, values in centrality_measures.items():
    plt.plot(list(values.keys()), list(values.values()), label=measure)
plt.xlabel('Node')
plt.ylabel('Centrality')
plt.title('Centrality Measures')
plt.legend()
plt.show()
clustering_coefficient = nx.average_clustering(G)
plt.figure(figsize=(6, 4))
plt.bar('Clustering Coefficient', clustering_coefficient, color='skyblue')
plt.ylabel('Clustering Coefficient')
plt.title('Average Clustering Coefficient')
plt.show()
communities = nx.algorithms.community.greedy_modularity_communities(G)
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=200)
plt.title('Community Detection')
plt.show()
shortest_paths = dict(nx.all_pairs_shortest_path_length(G))
path_lengths = [length for lengths in shortest_paths.values() for length in lengths.values()]
plt.figure(figsize=(8, 6))
plt.hist(path_lengths, bins=20, color='skyblue', alpha=0.7)
plt.xlabel('Shortest Path Length')
plt.ylabel('Frequency')
plt.title('Path Length Distribution')
plt.show()
assortativity = nx.degree_assortativity_coefficient(G)
print("Assortativity:", assortativity)
resilience = nx.algorithms.connectivity.node_connectivity(G)
print("Network Resilience:", resilience)
density = nx.density(G)
print("Graph Density:", density)
