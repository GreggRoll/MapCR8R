import PySimpleGUI as sg
import geopandas as gpd
import pandas as pd
import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt 

def HarryPlotter(path, lat_column, lon_column, export_path):
    """
    If variables not given in GUI it will default to values
    """
    df = pd.read_csv(path)
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Long_, df.Lat))
   
    plt.figure(figsize=(20,10))

    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.LAND, edgecolor='black')
    ax.add_feature(cartopy.feature.LAKES, edgecolor='black')
    ax.add_feature(cartopy.feature.RIVERS)
    ax.gridlines()

    gdf.plot(ax=ax, figsize=(8,12))

    plt.savefig(export_path)
    plt.show()

def input_sg():
    """
    Creates input window
    """
    #TODO use selection to determine map type
    #TODO load fiel then return pop up to plot columns
    #creating window
    layout = [
    [sg.Text('Please input the folder path')],
    [sg.Text('CSV File:', size=(18, 1)), sg.Input(), sg.FileBrowse()],
    [sg.Text('Lat name:', size=(18, 1)), sg.Input(), sg.Text()],
    [sg.Text('Long name:', size=(18, 1)), sg.Input(), sg.Text()],
    [sg.Text('Export to:', size=(18, 1)), sg.Input(), sg.FolderBrowse()],
    [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Map Plotter', layout)

    event, values = window.read()
    #incase fields are left blank or for testing purposes
    if values[0]:
        path = values[0]
    else:
        path = r"C:\Users\adams\Code\Data sets\time_series_covid19_deaths_US.csv"
    if values[1] and values[2]:
        lat_column, lon_column = values[1], values[2]
    else:
        lat_column, lon_column = "Lat", "Long_"
    if values[3]:
        export_path = values[3]
    else:
        export_path = r'C:\Users\adams\Code\Map creator\map.png'
    window.close()
    return path, lat_column, lon_column, export_path

path, lat_column, lon_column, export_path = input_sg()
#popup reads data input back to you
sg.popup('Results', "Path: " + path, "Lat: "+lat_column, "Long: "+lon_column, "export path: "+export_path)

HarryPlotter(path, lat_column, lon_column, export_path)