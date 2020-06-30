import PySimpleGUI as sg
import pandas as pd
import geopandas as gpd

#shp, lat/long
#file selector

#
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
            [sg.Text('File path: ', size=(18, 1)), sg.Input(), sg.FileBrowse()],
            [sg.Text('Geometry type', size=(18, 1)), sg.Radio('Lat/Long', 'Radio0', default=True), sg.Radio('Shape file', 'Radio0')],
            [sg.Submit(), sg.Cancel()]])
        event, values = window.read()
        get_cancel(event)
        #saying if no input use path specified
        if values[0]:
            path = values[0]
        else:
            path = r"C:\Users\adams\Code\Data sets\time_series_covid19_deaths_US.csv"
        if values[1]:
            geometry_type = 'Lat/Long'
        else:
            geometry_type = 'WKT'
        window.close()
        return path, geometry_type

    def return_options(df, geometry_type):
        #get columns
        column_list = df.columns
        
        if geometry_type == 'Lat/Long':
            #changing layout to not include lat/long for shape files
            layout = [
            [sg.Text('Lat name:', size=(18, 1)), sg.InputCombo(column_list), sg.Text()],
            [sg.Text('Long name:', size=(18, 1)), sg.InputCombo(column_list), sg.Text()],
            [sg.Text('Column to plot:', size=(18, 1)), sg.InputCombo(column_list), sg.Text()],
            [sg.Text('Please input boundaries as x0, x1, y0, y1', size=(30,1), text_color='RED')],
            [sg.Text('Map boundaries:', size=(18, 1)), sg.Input(), sg.Text()],
            [sg.Text('Export to:', size=(18, 1)), sg.Input(), sg.FolderBrowse()],
            [sg.Text('Plot type', size=(18, 1)), sg.Radio('Plot', 'Radio', default=True), sg.Radio('3D heat map', 'Radio')],
            [sg.Text('Legend : ', size=(18, 1)), sg.Checkbox('Yes', default=False)],
            [sg.Submit(), sg.Cancel()]]

        else:
            #shape does not support 3D heat maps
            layout = [
            [sg.Text('Column to plot:', size=(18, 1)), sg.InputCombo(column_list), sg.Text()],
            [sg.Text('Please input boundaries as x0, x1, y0, y1', size=(30,1), text_color='RED')],
            [sg.Text('Map boundaries:', size=(18, 1)), sg.Input(), sg.Text()],
            [sg.Text('Export to:', size=(18, 1)), sg.Input(), sg.FolderBrowse()],
            [sg.Text('Legend : ', size=(18, 1)), sg.Checkbox('Yes', default=False)],
            [sg.Submit(), sg.Cancel()]]
        #actually displaying window
        window = sg.Window('Map Plotter', layout)
        #reading values from window
        event, values = window.read()
        #if someone hits cancel for whatever reason
        get_cancel(event)
        #TODO radio buttons for lat/long, WKT
        #LAT/LONG
        if geometry_type == 'Lat/Long':
            if values[0] and values[1]:
                lat_column, lon_column = values[0], values[1]
            else:
                lat_column, lon_column = "Lat", "Long_"
            #Plot column
            if values[2]:
                plot_col = values[2]
            else:
                plot_col = None
            #Boundaries
            if values[3]:
                #boundaries comes in as a string, splitting into list then casting as ints
                boundaries = values[3].split(',')
                boundaries = [int(i) for i in boundaries]
            else:
                boundaries = [-180,180,-90,90]
            #export path
            if values[4]:
                export_path = values[4]
            else:
                export_path = r'C:\Users\adams\Code\Map creator\map.png'
            #Plot type
            #TODO add more plot types
            if values[5]:
                plot_type = 'point_plot'
            elif values[6]:
                plot_type = 'heat_map'
            legend = values[7]
            #must close window to continue script
            window.close()
            return lat_column, lon_column, plot_col, boundaries, export_path, plot_type, legend
        else:
            if values[0]:
                plot_col = values[0]
            else:
                plot_col = None
            #Boundaries
            if values[1]:
                #boundaries comes in as a string, splitting into list then casting as ints
                boundaries = values[1].split(',')
                boundaries = [int(i) for i in boundaries]
            else:
                boundaries = [-180,180,-90,90]
            #export path
            if values[2]:
                export_path = values[2]
            else:
                export_path = r'C:\Users\adams\Code\Map creator\map.png'
            legend = values[3]
            #must close window to continue script
            window.close()

            return plot_col, boundaries, export_path, legend

    #mapping path
    path, geometry_type = get_file()
    print(geometry_type)
    #testing CSV
    if geometry_type == 'Lat/Long':
        try: 
            df = pd.read_csv(path)
            #mapping variebles to definition variables
            lat_column, lon_column, plot_col, boundaries, export_path, plot_type, legend = return_options(df, geometry_type)
            return df, geometry_type, lat_column, lon_column, plot_col, boundaries, export_path, plot_type, legend
        except:
            sg.popup("Error",'invalid CSV')
            raise SystemExit(0)
    else:
        df = gpd.read_file(path)
        #mapping variebles to definition variables
        plot_col, boundaries, export_path, legend = return_options(df, geometry_type)
        return df, geometry_type, plot_col, boundaries, export_path, legend
