#purpose of this is to create a shape file wiwth world polygons

import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy

from grid_generator import grid_creator

def shape_generator(num_poly, min_max_long, min_max_lat, min_max_width, min_max_height):
    """
    Input min/max as tuples
    num_poly: number of polygons to generate in given bounds
    all values in decimal degrees
    """
    #list of lists
    lol = []

    for i in range(num_poly):
        #initializing row
        feature = [f"Polygon {i}"]
        #adding in number for later testing
        feature.append(np.random.randint(1, 999))
        #psuedo random x, y, length, and width
        x = np.random.uniform(min_max_long[0], min_max_long[1])
        y = np.random.uniform(min_max_lat[0], min_max_lat[1])
        length = np.random.uniform(min_max_width[0], min_max_width[1])
        height = np.random.uniform(min_max_height[0], min_max_height[1])
        #constructing polygon
        polygon1 = Polygon([
            (x,y), 
            (x+length,y),
            (x+length,y+height),
            (x,y+height),
            (x,y)])
        #adding to row
        feature.append(polygon1)
        #adding row to list of rows
        lol.append(feature)
    #casting as df
    df = pd.DataFrame(lol, columns=['PolyName', 'Value', 'geometry'])
    #turning into gdf
    return gpd.GeoDataFrame(df, geometry = 'geometry')


#saving as shp
#gdf.to_file(r"C:\Users\adams\Code\Data sets\1000_world_polygons.shp")

#1x1 grid of america
grid = grid_creator(25,52,-124,-66)
#this is america polys
gdf = shape_generator(100, (-124,-66), (25,52), (2,4), (0.5,2))

# dissolved = gpd.overlay(grid, gdf, how='left')
# print(dissolved.head())

#plotting
plt.figure(figsize=(20,10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.STATES)
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.LAND, edgecolor='black')
#ax.add_feature(cartopy.feature.LAKES, edgecolor='black')
ax.add_feature(cartopy.feature.RIVERS)
ax.gridlines()

gdf.plot(ax=ax, column='Value', legend=True)
plt.savefig("Shape_Generator.png")
plt.show()