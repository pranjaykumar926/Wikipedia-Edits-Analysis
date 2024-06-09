import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

file_path = 'cleaned_source_tgt_val.csv'
data = pd.read_csv(file_path)
geolocator = Nominatim(user_agent="geoapiExercises")
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
countries = pd.concat([data['Country1'], data['Country2']]).unique()
coordinates = {country: get_lat_long(country) for country in countries}
coordinates = {country: coords for country, coords in coordinates.items() if coords}
def calculate_distance(country1, country2):
    coords_1 = coordinates.get(country1)
    coords_2 = coordinates.get(country2)
    if coords_1 and coords_2:
        return geodesic(coords_1, coords_2).kilometers
    return None
data['Geographical_Distance'] = data.apply(
    lambda row: calculate_distance(row['Country1'], row['Country2']), axis=1)
cleaned_data = data.dropna(subset=['Geographical_Distance'])
output_file_path = 'country_geographical_distances.csv'
cleaned_data.to_csv(output_file_path, index=False)
print(cleaned_data.head())
