import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import random

file_path = 'country_geographical_distances.csv' 
data = pd.read_csv(file_path)


weight_graph = nx.Graph()
for index, row in data.iterrows():
    weight_graph.add_edge(row['Country1'], row['Country2'], weight=row['Weight'])
geographical_distance_graph = nx.Graph()
for index, row in data.iterrows():
    geographical_distance_graph.add_edge(row['Country1'], row['Country2'], weight=row['Geographical_Distance'])
random_graph = nx.Graph()
for edge in data[['Country1', 'Country2']].values:
    random_graph.add_edge(edge[0], edge[1], weight=random.randint(1, 10))
def visualize_graph(G, title):
    pos = nx.spring_layout(G, seed=42)  
    weights = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.title(title)
    plt.show()
visualize_graph(weight_graph, 'Weight Graph')
visualize_graph(geographical_distance_graph, 'Geographical Distance Graph')
edge_labels = nx.get_edge_attributes(random_graph, 'weight')
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(random_graph)
nx.draw(random_graph, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', font_size=10)
nx.draw_networkx_edge_labels(random_graph, pos, edge_labels=edge_labels)
plt.title("Random Graph with Random Edge Weights")
plt.show()
