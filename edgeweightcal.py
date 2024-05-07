import pandas as pd
from collections import defaultdict

def calculate_pair_weights(df):
    edge_weights = defaultdict(int)
    for index, row in df.iterrows():
        previous_item = None
        for item in row.dropna():
            if previous_item is not None and previous_item != item:
                pair = (previous_item, item)
                edge_weights[pair] += 1
            previous_item = item
    return edge_weights

try:
    column_names = [f"col{i}" for i in range(200)]  
    df = pd.read_csv('languageedition.csv', sep=';', header=None, names=column_names, engine='python')
    weights = calculate_pair_weights(df)
    if weights:
        for pair, weight in weights.items():
            print(f"Edge {pair} has weight {weight}")
    else:
        print("No weights calculated, possibly due to data issues.")
except pd.errors.ParserError as pe:
    print(f"Parser error: {pe}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")