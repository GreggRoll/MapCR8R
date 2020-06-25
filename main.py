from GUI import input_sg
from plotter import HarryPlotter
import PySimpleGUI as sg

def main():
    df, lat_column, lon_column, boundaries, export_path, plot_type = input_sg()
    #popup reads data input back to you
    sg.popup('Results', "DataFrame head: ",df.head(), "Lat: "+lat_column, "Long: "+lon_column, "Boundaries :"+str(boundaries),"export path: "+export_path, "Plot type : "+plot_type)
    #runs plotter
    HarryPlotter(df, lat_column, lon_column, boundaries, export_path, plot_type)

if __name__ == "__main__":
    # execute only if run as a script
    main()