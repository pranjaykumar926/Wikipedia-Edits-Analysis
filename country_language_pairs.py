import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def create_language_to_country_mapping():
    # This is a simplified version of the mapping
    return {
        'en': ['USA', 'Canada'],
        'sv': ['Sweden'],
        'fr': ['France', 'Canada'],
        'nl': ['Netherlands'],
        'zh': ['China'],
        'es': ['Spain', 'Mexico']
    }

def replace_languages_with_countries(row, mapping):
    source_countries = mapping.get(row['Source'], [row['Source']])
    target_countries = mapping.get(row['Target'], [row['Target']])
    return pd.DataFrame([(source, target, row['Weight']) for source in source_countries for target in target_countries],
                        columns=['country1', 'country2', 'weight'])

def process_data(data, mapping):
    return pd.concat([replace_languages_with_countries(row, mapping) for index, row in data.iterrows()])

def save_to_csv(data, output_file_path):
    data.to_csv(output_file_path, index=False)

def main(input_file_path, output_file_path):
    # Load the data
    data = load_data(input_file_path)
    
    # Create the language to country mapping
    mapping = create_language_to_country_mapping()
    
    # Process the data
    expanded_data = process_data(data, mapping)
    
    # Save the expanded data to the CSV file
    save_to_csv(expanded_data, output_file_path)
    print(f"Data successfully saved to {output_file_path}")

if __name__ == "__main__":
    input_file_path = 'source_tgt_val_modified.csv'  # Replace with the actual path to your input file
    output_file_path = 'country_language_pairs.csv'  # Desired output file path
    main(input_file_path, output_file_path)
