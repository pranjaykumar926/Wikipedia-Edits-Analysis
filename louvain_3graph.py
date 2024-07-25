import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import random
import community as community_louvain

file_path = 'country_geographical_distances.csv'
data = pd.read_csv('country_geographical_distances.csv')

weight_graph = nx.Graph()
for index, row in data.iterrows():
    weight_graph.add_edge(row['Country1'], row['Country2'], weight=row['Weight'])

geographical_distance_graph = nx.Graph()
for index, row in data.iterrows():
    geographical_distance_graph.add_edge(row['Country1'], row['Country2'], weight=row['Geographical_Distance'])

random_graph = nx.Graph()
for edge in data[['Country1', 'Country2']].values:
    random_graph.add_edge(edge[0], edge[1], weight=random.randint(1, 10))

def visualize_communities(G, title):
    partition = community_louvain.best_partition(G, weight='weight')
    pos = nx.spring_layout(G, seed=42)
    cmap = plt.get_cmap('viridis')
    nx.draw(G, pos, node_color=[partition[node] for node in G.nodes()], 
            node_size=500, cmap=cmap, with_labels=True, font_size=10, font_weight='bold')
    plt.title(title)
    plt.show()

visualize_communities(weight_graph, 'Communities in Weight Graph')
visualize_communities(geographical_distance_graph, 'Communities in Geographical Distance Graph')
visualize_communities(random_graph, 'Communities in Random Graph')
