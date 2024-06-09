import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Load the CSV file
file_path = 'cleaned_source_tgt_val.csv'
data = pd.read_csv(file_path)

# Initialize the geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Function to get latitude and longitude for a given country
def get_lat_long(country):
    try:
        location = geolocator.geocode(country)
        if location:
            print(f"Coordinates for {country}: {location.latitude}, {location.longitude}")
            return (location.latitude, location.longitude)
        else:
            print(f"Coordinates for {country} not found.")
    except Exception as e:
        print(f"Error fetching coordinates for {country}: {e}")
    return None

# Get unique list of countries
countries = pd.concat([data['Country1'], data['Country2']]).unique()

# Get coordinates for each country
coordinates = {country: get_lat_long(country) for country in countries}
coordinates = {country: coords for country, coords in coordinates.items() if coords}

# Function to calculate the distance between two countries
def calculate_distance(country1, country2):
    coords_1 = coordinates.get(country1)
    coords_2 = coordinates.get(country2)
    if coords_1 and coords_2:
        return geodesic(coords_1, coords_2).kilometers
    return None

# Calculate geographical distance for each row in the dataframe
data['Geographical_Distance'] = data.apply(
    lambda row: calculate_distance(row['Country1'], row['Country2']), axis=1)

# Drop rows with missing geographical distance
cleaned_data = data.dropna(subset=['Geographical_Distance'])

# Save the cleaned data to a new CSV file
output_file_path = 'country_geographical_distances.csv'
cleaned_data.to_csv(output_file_path, index=False)

# Print the first few rows of the cleaned data
print(cleaned_data.head())
