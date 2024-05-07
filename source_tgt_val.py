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
    edge_weights = calculate_pair_weights(df)
    filtered_edge_weights = {pair: weight for pair, weight in edge_weights.items() if weight >= 5}
    filtered_df = pd.DataFrame(filtered_edge_weights.items(), columns=['Nodes', 'Weight'])
    filtered_df[['Source', 'Target']] = pd.DataFrame(filtered_df['Nodes'].tolist(), index=filtered_df.index)
    filtered_df.drop(columns=['Nodes'], inplace=True)
    filtered_df = filtered_df[['Source', 'Target', 'Weight']]
    filtered_df.to_csv('source_tgt_val.csv', index=False)

    print("Filtered CSV file created successfully.")
except pd.errors.ParserError as pe:
    print(f"Parser error: {pe}")
except Exception as e:
    print(f"An error occurred: {e}")