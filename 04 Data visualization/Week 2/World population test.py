import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the world map
gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Load the dataset
df = pd.read_csv("world_population.csv")

# Merge population data with geospatial data
gdf = gdf.merge(df, left_on='name', right_on='Country/Territory', how='left')

# Calculate population density
gdf['density'] = gdf['2022 Population'] / gdf['Area (km²)']

# Normalize density for scaling
min_size, max_size = 0.5, 5  # Scale factor range
gdf['size_factor'] = np.interp(gdf['density'], (gdf['density'].min(), gdf['density'].max()), (min_size, max_size))

# Plot the transformed map
fig, ax = plt.subplots(figsize=(12, 8))
for _, row in gdf.iterrows():
    if isinstance(row['geometry'], float):  # Skip NaN geometries
        continue
    country = gpd.GeoSeries(row['geometry'])
    country = country.scale(row['size_factor'], row['size_factor'], origin='center')
    country.plot(ax=ax, color=plt.cm.Reds(row['size_factor'] / max_size), edgecolor='black')

plt.title("World Map Scaled by Population Density (2022)")
plt.axis("off")
plt.show()
