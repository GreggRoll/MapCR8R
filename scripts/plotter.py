import geopandas as gpd
import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt 

import geoplot

def lat_lon_plotter(df, plot_name, lat_column, lon_column, plot_col, boundaries, export_path, plot_type, legend):
        """
        If variables not given in GUI it will default to values
        """
        gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Long_, df.Lat))
        #drawing figure with width of 20in and height of 10in
        plt.figure(figsize=(20,10))
        #TODO allow selection of projection
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.set_title(plot_name)
        ax.set_extent(boundaries)
        ax.add_feature(cartopy.feature.OCEAN)
        ax.add_feature(cartopy.feature.LAND, edgecolor='black')
        ax.add_feature(cartopy.feature.LAKES, edgecolor='black')
        ax.add_feature(cartopy.feature.RIVERS)
        #TODO allow gridlines toggle
        ax.gridlines()
        #plotting geodataframe on AX
        if plot_type == 'point_plot':
                gdf.plot(ax=ax, column=plot_col, legend=legend)
        #3D heat map using kdeplot density closeness
        elif plot_type == 'heat_map':
                #boundaries wwere not reading from set extent, had to refactor because geoplot.kdeplot uses x0,y0,x1,y1
                geoplot.kdeplot(gdf, ax=ax, shade=True, cmap='Reds', extent=[boundaries[0], boundaries[2], boundaries[1], boundaries[3]])
        #saving to plot path
        plt.savefig(export_path)
        #this shows the window that we see
        plt.show()

def shp_plotter(gdf, plot_name, plot_col, boundaries, export_path, legend):
        """
        can turn these two into 1 later, idk if best practice is to keep them seperate or not
        """
        plt.figure(figsize=(20,10))

        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.set_extent(boundaries)
        ax.set_title(plot_name)
        ax.add_feature(cartopy.feature.OCEAN)
        ax.add_feature(cartopy.feature.LAND, edgecolor='black')
        ax.add_feature(cartopy.feature.LAKES, edgecolor='black')
        ax.add_feature(cartopy.feature.RIVERS)

        ax.gridlines()
        
        if plot_col:
                gdf.plot(ax=ax, column=plot_col, legend=legend)
        else:
                gdf.plot(ax=ax)

        plt.savefig(export_path)
        plt.show()