import requests
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString
import folium
import time
import os
from dotenv import load_dotenv

# Suppress warnings for cleaner output
import warnings
warnings.filterwarnings('ignore')

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('LTA_API_KEY')

# Verify that the API_KEY was loaded
if not API_KEY:
    raise ValueError("LTA_API_KEY not found. Please check your .env file.")
else:
    print("LTA_API_KEY successfully loaded.")

headers = {'AccountKey': API_KEY, 'accept': 'application/json'}

# Function to fetch all bus stops with pagination
def get_bus_stops():
    bus_stops = []
    skip = 0
    print("Fetching bus stops data...")
    while True:
        url = f'https://datamall2.mytransport.sg/ltaodataservice/BusStops?$skip={skip}'
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            print("Response:", response.text)
            break
        try:
            data = response.json()
        except ValueError:
            print("Error: Unable to decode JSON response.")
            print("Response Text:", response.text)
            break
        if not data.get('value'):
            break
        bus_stops.extend(data['value'])
        print(f"Fetched {len(bus_stops)} bus stops so far...")
        skip += 500
        time.sleep(0.2)
    bus_stops_df = pd.DataFrame(bus_stops)
    print(f"Total bus stops retrieved: {len(bus_stops_df)}\n")
    return bus_stops_df

# Function to fetch all bus routes with pagination
def get_bus_routes():
    bus_routes = []
    skip = 0
    print("Fetching bus routes data...")
    while True:
        url = f'https://datamall2.mytransport.sg/ltaodataservice/BusRoutes?$skip={skip}'
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            print("Response:", response.text)
            break
        try:
            data = response.json()
        except ValueError:
            print("Error: Unable to decode JSON response.")
            print("Response Text:", response.text)
            break
        if not data.get('value'):
            break
        bus_routes.extend(data['value'])
        print(f"Fetched {len(bus_routes)} bus routes so far...")
        skip += 500
        time.sleep(0.2)
    bus_routes_df = pd.DataFrame(bus_routes)
    print(f"Total bus routes retrieved: {len(bus_routes_df)}\n")
    return bus_routes_df

# Fetch and prepare bus stops and bus routes data
bus_stops_df = get_bus_stops()
bus_routes_df = get_bus_routes()

# Convert Latitude and Longitude to numeric for bus stops
bus_stops_df['Latitude'] = pd.to_numeric(bus_stops_df['Latitude'], errors='coerce')
bus_stops_df['Longitude'] = pd.to_numeric(bus_stops_df['Longitude'], errors='coerce')

# Create GeoDataFrame for bus stops
bus_stops_gdf = gpd.GeoDataFrame(
    bus_stops_df,
    geometry=gpd.points_from_xy(bus_stops_df['Longitude'], bus_stops_df['Latitude']),
    crs='EPSG:4326'
)

# Merge bus routes with bus stops to get coordinates
print("Merging bus routes with bus stops...")
merged_data = pd.merge(bus_routes_df, bus_stops_df, on='BusStopCode', how='left', suffixes=('_route', '_stop'))
merged_data.dropna(subset=['Latitude', 'Longitude'], inplace=True)
print(f"Total merged records: {len(merged_data)}\n")

# Create GeoDataFrame for bus routes points
print("Creating GeoDataFrame for bus routes...")
merged_data['geometry'] = merged_data.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)
bus_routes_points_gdf = gpd.GeoDataFrame(merged_data, geometry='geometry', crs='EPSG:4326')

# Create LineStrings for each bus route
print("Creating LineStrings for each bus route...")
bus_routes_lines = bus_routes_points_gdf.sort_values(['ServiceNo', 'Direction', 'StopSequence'])
bus_routes_lines = bus_routes_lines.groupby(['ServiceNo', 'Direction'])['geometry'].apply(lambda x: LineString(x.tolist()))
bus_routes_lines = bus_routes_lines.reset_index()
bus_routes_lines_gdf = gpd.GeoDataFrame(bus_routes_lines, geometry='geometry', crs='EPSG:4326')

# Load MRT station data from shapefile
mrt_stations_gdf = gpd.read_file('./trainstation/RapidTransitSystemStation.shp')

# Convert MRT station data to WGS84 (latitude/longitude)
mrt_stations_gdf = mrt_stations_gdf.to_crs(epsg=4326)
mrt_station_csv =mrt_stations_gdf.to_csv
print(f"Total train stations loaded: {len(mrt_stations_gdf)}\n")

# Extract centroids if geometries are polygons
mrt_stations_gdf['geometry'] = mrt_stations_gdf['geometry'].apply(
    lambda geom: geom.centroid if geom.geom_type in ['Polygon', 'MultiPolygon'] else geom
)

# Visualization: Create Folium map
print("Creating Folium map...")
m = folium.Map(location=[1.3521, 103.8198], zoom_start=12)

# Add MRT stations to the map as blue markers
print("Adding MRT stations to the map...")
for _, row in mrt_stations_gdf.iterrows():
    if row.geometry.geom_type == 'Point':
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=3,
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.7,
            popup=row['STN_NAM'],  # Assuming 'STN_NAM' is the station name column
            tooltip=row['STN_NAM']
        ).add_to(m)

# Add bus routes to the map with popups showing the ServiceNo
print("Adding bus routes to the map...")
for _, row in bus_routes_lines_gdf.iterrows():
    service_no = row['ServiceNo']
    folium.GeoJson(
        row['geometry'],
        style_function=lambda x: {'color': 'green', 'weight': 1, 'opacity': 0.5},
        tooltip=f"Bus Service No: {service_no}",
        popup=f"Bus Service No: {service_no}"
    ).add_to(m)

# Add layer control to the map
folium.LayerControl().add_to(m)

# Save the map to an HTML file
map_filename = './bus_mrt_map/mrt_bus_routes_map.html'
m.save(map_filename)
print(f"Map saved as '{map_filename}'.\n")

print("Visualization complete! Open the HTML file to view the map.")
