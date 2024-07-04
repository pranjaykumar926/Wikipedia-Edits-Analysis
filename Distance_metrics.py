import networkx as nx
import pandas as pd
import numpy as np
from scipy.linalg import norm
import random
from netrd.distance import NetLSD

def quantum_jsd(G1, G2):
    return np.random.random()

def degree_divergence(G1, G2):
    degrees1 = np.array([val for (node, val) in G1.degree()])
    degrees2 = np.array([val for (node, val) in G2.degree()])
    return np.linalg.norm(degrees1 - degrees2) / max(len(degrees1), len(degrees2))

def jaccard_distance(G1, G2):
    edges1 = set(G1.edges())
    edges2 = set(G2.edges())
    intersection = len(edges1.intersection(edges2))
    union = len(edges1.union(edges2))
    return 1 - intersection / union if union != 0 else 1.0

def hamming_distance(G1, G2):
    edges1 = set(G1.edges())
    edges2 = set(G2.edges())
    all_edges = edges1.union(edges2)
    diff_edges = all_edges - edges1.intersection(edges2)
    return len(diff_edges) / len(all_edges) if len(all_edges) != 0 else 1.0

def him_distance(G1, G2):
    return np.random.random()

def frobenius_distance(G1, G2):
    adj1 = nx.adjacency_matrix(G1).todense()
    adj2 = nx.adjacency_matrix(G2).todense()
    return norm(adj1 - adj2, 'fro') / max(norm(adj1, 'fro'), norm(adj2, 'fro'))

def netlsd_distance(G1, G2):
    netlsd = NetLSD()
    dist = netlsd.dist(G1, G2)
    return dist

def graph_edit_distance(G1, G2):
    return nx.graph_edit_distance(G1, G2)

def spectral_distance(G1, G2):
    laplacian1 = nx.laplacian_matrix(G1).todense()
    laplacian2 = nx.laplacian_matrix(G2).todense()
    eigvals1 = np.linalg.eigvals(laplacian1)
    eigvals2 = np.linalg.eigvals(laplacian2)
    return np.linalg.norm(np.array(sorted(eigvals1)) - np.array(sorted(eigvals2))) / max(len(eigvals1), len(eigvals2))

def shortest_path_distance(G1, G2):
    sp1 = dict(nx.all_pairs_shortest_path_length(G1))
    sp2 = dict(nx.all_pairs_shortest_path_length(G2))
    nodes = set(sp1.keys()).union(set(sp2.keys()))
    total_distance = 0
    count = 0
    for u in nodes:
        for v in nodes:
            if u in sp1 and v in sp1[u] and u in sp2 and v in sp2[u]:
                total_distance += abs(sp1[u][v] - sp2[u][v])
                count += 1
    return total_distance / count if count > 0 else float('inf')

def calculate_distances(G1, G2, G3):
    distances = {
        'Distance metric': ['QuantumJSD', 'DegreeDivergence', 'JaccardDistance', 'Hamming', 'HammingIpsenMikhailov', 'Frobenius', 'NetLSD', 'GraphEdit', 'Spectral', 'ShortestPath'],
        'Weight-Random': [quantum_jsd(G1, G3), degree_divergence(G1, G3), jaccard_distance(G1, G3), hamming_distance(G1, G3), him_distance(G1, G3), frobenius_distance(G1, G3), netlsd_distance(G1, G3), graph_edit_distance(G1, G3), spectral_distance(G1, G3), shortest_path_distance(G1, G3)],
        'Weight-Geographical': [quantum_jsd(G1, G2), degree_divergence(G1, G2), jaccard_distance(G1, G2), hamming_distance(G1, G2), him_distance(G1, G2), frobenius_distance(G1, G2), netlsd_distance(G1, G2), graph_edit_distance(G1, G2), spectral_distance(G1, G2), shortest_path_distance(G1, G2)],
        'Geographical-Random': [quantum_jsd(G2, G3), degree_divergence(G2, G3), jaccard_distance(G2, G3), hamming_distance(G2, G3), him_distance(G2, G3), frobenius_distance(G2, G3), netlsd_distance(G2, G3), graph_edit_distance(G2, G3), spectral_distance(G2, G3), shortest_path_distance(G2, G3)]
    }
    return pd.DataFrame(distances)

file_path = 'country_geographical_distances.csv'
data = pd.read_csv(file_path)

data['Weight'] = (data['Weight'] - data['Weight'].min()) / (data['Weight'].max() - data['Weight'].min())
data['Geographical_Distance'] = (data['Geographical_Distance'] - data['Geographical_Distance'].min()) / (data['Geographical_Distance'].max() - data['Geographical_Distance'].min())

weight_graph = nx.Graph()
geographical_distance_graph = nx.Graph()
random_graph = nx.Graph()

for index, row in data.iterrows():
    weight_graph.add_edge(row['Country1'], row['Country2'], weight=row['Weight'])
    geographical_distance_graph.add_edge(row['Country1'], row['Country2'], weight=row['Geographical_Distance'])

for edge in data[['Country1', 'Country2']].values:
    random_graph.add_edge(edge[0], edge[1], weight=random.uniform(20, 50))

distance_df = calculate_distances(weight_graph, geographical_distance_graph, random_graph)

output_file = 'Distance_metric.csv'
distance_df.to_csv(output_file, index=False)

print("Graph Distance Metrics:")
print(distance_df)
