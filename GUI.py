import PySimpleGUI as sg
import pandas as pd


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
        [sg.Text('Please input boundaries as x0, x1, y0, y1', size=(30,1), text_color='RED')],
        [sg.Text('Map boundaries:', size=(18, 1)), sg.Input(), sg.Text()],
        [sg.Text('Export to:', size=(18, 1)), sg.Input(), sg.FolderBrowse()],
        [sg.Text('Plot type', size=(18, 1)), sg.Radio('Plot', 'Radio', default=True), sg.Radio('3D heat map', 'Radio')],
        [sg.Submit(), sg.Cancel()]]
        #actually displaying window
        window = sg.Window('Map Plotter', layout)
        #reading values from window
        event, values = window.read()
        #if someone hits cancel for whatever reason
        get_cancel(event)
        #testing to
        if values[0] and values[1]:
            lat_column, lon_column = values[0], values[1]
        else:
            lat_column, lon_column = "Lat", "Long_"
        if values[2]:
            #boundaries comes in as a string, splitting into list then casting as ints
            boundaries = values[2].split(',')
            boundaries = [int(i) for i in boundaries]
        else:
            boundaries = [-180,180,-90,90]
        if values[3]:
            export_path = values[3]
        else:
            export_path = r'C:\Users\adams\Code\Map creator\map.png'
        #TODO add more plot types
        if values[4]:
            plot_type = 'plot'
        elif values[5]:
            plot_type = 'heat_map'
        #must close window to continue script
        window.close()

        return lat_column, lon_column, boundaries, export_path, plot_type

    #mapping path
    path = get_file()
    #testing CSV
    try: 
        df = pd.read_csv(path)
    except:
        sg.popup("Error",'invalid CSV')
        raise SystemExit(0)

    #mapping variebles to definition variables
    lat_column, lon_column, boundaries, export_path, plot_type = return_options(df)

    return df, lat_column, lon_column, boundaries, export_path, plot_type