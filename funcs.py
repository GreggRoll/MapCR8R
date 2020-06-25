import PySimpleGUI as sg
import geopandas as gpd
import pandas as pd
import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt 

def HarryPlotter(df, lat_column, lon_column, boundaries, export_path):
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
    gdf.plot(ax=ax)
    #saving to plot path
    plt.savefig(export_path)
    #this shows the window that we see
    plt.show()

def input_sg():
    """
    Creates input window
    """
    #TODO use selection to determine map type
    #TODO load field then return pop up to plot columns
    
    # run to determine cancel
    def get_cancel(event):
        if event == 'Cancel':
            sg.popup("Error",'Why you no want to use me?')
            raise SystemExit(0)
    
    #initial file input
    def get_file():
        window = sg.Window('Map Plotter', [
            [sg.Text('Please input the folder path')],
            [sg.Text('CSV File:', size=(18, 1)), sg.Input(), sg.FileBrowse()],
            [sg.Submit(), sg.Cancel()]])
        event, values = window.read()
        get_cancel(event)
        #saying if no input use path specified
        if values[0]:
            path = values[0]
        else:
            path = r"C:\Users\adams\Code\Data sets\time_series_covid19_deaths_US.csv"
        window.close()
        return path

    def return_options(df):

        column_list = df.columns

        layout = [
        [sg.Text('Lat name:', size=(18, 1)), sg.InputCombo(column_list), sg.Text()],
        [sg.Text('Long name:', size=(18, 1)), sg.InputCombo(column_list), sg.Text()],
        [sg.Text('Please input boundaries as (x0, x1)', size=(30,1), text_color='RED')],
        [sg.Text('X boundaries:', size=(18, 1)), sg.Input(), sg.Text()],
        [sg.Text('Y boundaries:', size=(18, 1)), sg.Input(), sg.Text()],
        [sg.Text('Export to:', size=(18, 1)), sg.Input(), sg.FolderBrowse()],
        [sg.Submit(), sg.Cancel()]]
        #actually displaying window
        window = sg.Window('Map Plotter', layout)
        #reading values from window
        event, values = window.read()
        #if someone hits cancel for whatever reason
        get_cancel(event)
        #testing to
        if values[0] and values[1]:
            lat_column, lon_column = values[1], values[2]
        else:
            lat_column, lon_column = "Lat", "Long_"
        if values[2] and values[3]:
            boundaries = [i for i in values[2]] + [i for i in values[3]]
        else:
            boundaries = [-180,180,-90,90]
        if values[3]:
            export_path = values[3]
        else:
            export_path = r'C:\Users\adams\Code\Map creator\map.png'
        #must close window to continue script
        window.close()

        return lat_column, lon_column, boundaries, export_path

    #mapping path
    path = get_file()
    #testing CSV
    try: 
        df = pd.read_csv(path)
    except:
        sg.popup("Error",'invalid CSV')
        raise SystemExit(0)

    #mapping variebles to definition variables
    lat_column, lon_column, boundaries, export_path = return_options(df)

    return df, lat_column, lon_column, boundaries, export_path

df, lat_column, lon_column, boundaries, export_path = input_sg()
#popup reads data input back to you
sg.popup('Results', "DataFrame head: ",df.head(), "Lat: "+lat_column, "Long: "+lon_column, "Boundaries :"+str(boundaries),"export path: "+export_path)
#runs plotter
HarryPlotter(df, lat_column, lon_column, boundaries, export_path)