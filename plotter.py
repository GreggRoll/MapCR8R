import geopandas as gpd
import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt 

import geoplot

def HarryPlotter(df, lat_column, lon_column, boundaries, export_path, plot_type):
    """
    If variables not given in GUI it will default to values
    """
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Long_, df.Lat))
    #drawing figure with width of 20in and height of 10in
    plt.figure(figsize=(20,10))
    #TODO allow selection of projection
    ax = plt.axes(projection=ccrs.PlateCarree())
    #TODO fix this
    ax.set_extent(boundaries)
    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.LAND, edgecolor='black')
    ax.add_feature(cartopy.feature.LAKES, edgecolor='black')
    ax.add_feature(cartopy.feature.RIVERS)
    #TODO allow gridlines toggle
    ax.gridlines()
    #plotting geodataframe on AX
    if plot_type == 'plot':
            gdf.plot(ax=ax)
    elif plot_type == 'heat_map':
            geoplot.kdeplot(gdf, ax=ax, shade=True, cmap='Reds')
    #saving to plot path
    plt.savefig(export_path)
    #this shows the window that we see
    plt.show()
