import pandas as pd
import networkx as nx

# Load the cleaned data
file_path = 'country_geographical_distances.csv'
data = pd.read_csv(file_path)

# Create the first graph with Weight as edge weight
G1 = nx.Graph()
for index, row in data.iterrows():
    G1.add_edge(row['Country1'], row['Country2'], weight=row['Weight'])

# Create the second graph with Geographical_Distance as edge weight
G2 = nx.Graph()
for index, row in data.iterrows():
    G2.add_edge(row['Country1'], row['Country2'], weight=row['Geographical_Distance'])

# Function to calculate metrics for a given graph
def get_graph_metrics(G):
    density = nx.density(G)
    clustering_coefficient = nx.average_clustering(G)
    try:
        diameter = nx.diameter(G)
    except nx.NetworkXError:
        diameter = float('inf')
    if nx.is_connected(G):
        avg_shortest_path_length = nx.average_shortest_path_length(G)
    else:
        avg_shortest_path_length = float('inf')
    degree_centrality = nx.degree_centrality(G)
    degree_centrality_avg = sum(degree_centrality.values()) / len(degree_centrality)
    return density, clustering_coefficient, diameter, avg_shortest_path_length, degree_centrality_avg

# Calculate metrics for both graphs
metrics_G1 = get_graph_metrics(G1)
metrics_G2 = get_graph_metrics(G2)

# Create DataFrame to store results
metrics_df = pd.DataFrame({
    'Property': ['Density', 'Average Clustering Coefficient', 'Diameter', 'Average Shortest Path Length', 'Average Degree Centrality'],
    'Graph1': metrics_G1,
    'Graph2': metrics_G2
})

# Save the results to a CSV file
output_file_path = 'graph_similarity_metrics.csv'
metrics_df.to_csv(output_file_path, index=False)

print(f"Metrics have been calculated and saved to {output_file_path}")
print(metrics_df)
