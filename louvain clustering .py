import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain

file_path = 'country_geographical_distances.csv'
data = pd.read_csv(file_path)
G1 = nx.Graph()
for index, row in data.iterrows():
    G1.add_edge(row['Country1'], row['Country2'], weight=row['Weight'])
partition1 = community_louvain.best_partition(G1, weight='weight')
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G1)
colors1 = [partition1[node] for node in G1.nodes()]
nx.draw(G1, pos, node_color=colors1, with_labels=True, node_size=5000, font_size=15, cmap=plt.cm.rainbow)
labels1 = nx.get_edge_attributes(G1, 'weight')
nx.draw_networkx_edge_labels(G1, pos, edge_labels=labels1)
plt.title('Louvain Clustering on Graph with Weights')
plt.show()
G2 = nx.Graph()
for index, row in data.iterrows():
    G2.add_edge(row['Country1'], row['Country2'], weight=row['Geographical_Distance'])
partition2 = community_louvain.best_partition(G2, weight='weight')

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G2)
colors2 = [partition2[node] for node in G2.nodes()]
nx.draw(G2, pos, node_color=colors2, with_labels=True, node_size=5000, font_size=15, cmap=plt.cm.rainbow)
labels2 = nx.get_edge_attributes(G2, 'weight')
nx.draw_networkx_edge_labels(G2, pos, edge_labels=labels2)
plt.title('Louvain Clustering on Graph with Geographical Distances')
plt.show()
