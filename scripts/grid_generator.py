#purpose of this is to create a shapefile of 1x1 deegree polygons
from shapely.geometry import Polygon
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy

def grid_creator(start_lat, end_lat, start_long, end_long):
    """
    Creates 1 degree gridcells starting at the start lat assigns name to each
    """
    #List of polys
    lop = []
    #initialize coutner for poly name
    counter = 0
    while start_lat <= end_lat:
        #reset long and increase lat 1
        long = start_long
        while long <= end_long:
            #wkt fromat
            lop.append([f"Grid cell {counter}", Polygon([(long,start_lat), (long+1,start_lat), (long+1,start_lat+1), (long,start_lat+1), (long,start_lat)])])
            #increase long for next loop
            long += 1
            counter += 1
        #increase lat for next loop
        start_lat += 1

    df = pd.DataFrame(lop, columns='Name geometry'.split())
    
    return gpd.GeoDataFrame(df, geometry='geometry')

# gdf = grid_creator(25,52,-124,-66)

# plt.figure(figsize=(20,10))
# ax = plt.axes(projection=ccrs.PlateCarree())
# ax.add_feature(cartopy.feature.STATES)
# ax.add_feature(cartopy.feature.OCEAN)
# ax.add_feature(cartopy.feature.LAND, edgecolor='black')
# #ax.add_feature(cartopy.feature.LAKES, edgecolor='black')
# ax.add_feature(cartopy.feature.RIVERS)
# ax.gridlines()

# gdf.plot(ax=ax, cmap='OrRd')
# plt.show()