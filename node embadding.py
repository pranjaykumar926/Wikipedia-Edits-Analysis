import networkx as nx
from node2vec import Node2Vec
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

filtered_df = pd.read_csv('source_tgt_val.csv')
G = nx.from_pandas_edgelist(filtered_df, 'Source', 'Target', ['Weight'], create_using=nx.DiGraph())

node2vec = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=4)
model = node2vec.fit(window=10, min_count=1, batch_words=4)
node_embeddings = {node: model.wv[node] for node in G.nodes()}
embeddings = np.array([emb for emb in node_embeddings.values()])
tsne = TSNE(n_components=2, perplexity=30, n_iter=300)
embeddings_2d = tsne.fit_transform(embeddings)
plt.figure(figsize=(8, 6))
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], alpha=0.5)
for i, node in enumerate(G.nodes()):
    plt.annotate(node, (embeddings_2d[i, 0], embeddings_2d[i, 1]))

plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.title('Node2Vec Embeddings Visualization')
plt.grid(True)
plt.show()
node_names = list(G.nodes())
node_vectors = [node_embeddings[node] for node in node_names]
df = pd.DataFrame({'Language': node_names, 'Vector': node_vectors})
df.to_csv('language_vectors.csv', index=False)
