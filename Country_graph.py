import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
file_path = 'country_geographical_distances.csv'
data = pd.read_csv(file_path)
G1 = nx.Graph()
for index, row in data.iterrows():
    G1.add_edge(row['Country1'], row['Country2'], weight=row['Weight'])
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G1)
nx.draw(G1, pos, with_labels=True, node_size=5000, node_color="skyblue", font_size=15)
labels = nx.get_edge_attributes(G1, 'weight')
nx.draw_networkx_edge_labels(G1, pos, edge_labels=labels)
plt.title('Graph with Weights as Edge Weights')
plt.show()

G2 = nx.Graph()
for index, row in data.iterrows():
    G2.add_edge(row['Country1'], row['Country2'], weight=row['Geographical_Distance'])
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G2)
nx.draw(G2, pos, with_labels=True, node_size=5000, node_color="lightgreen", font_size=15)
labels = nx.get_edge_attributes(G2, 'weight')
nx.draw_networkx_edge_labels(G2, pos, edge_labels=labels)
plt.title('Graph with Geographical Distances as Edge Weights')
plt.show()
