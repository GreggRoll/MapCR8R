from funcs import HarryPlotter, input_sg
import PySimpleGUI as sg

def main():
    df, lat_column, lon_column, boundaries, export_path = input_sg()
    #popup reads data input back to you
    sg.popup('Results', "DataFrame head: ",df.head(), "Lat: "+lat_column, "Long: "+lon_column, "Boundaries :"+str(boundaries),"export path: "+export_path)
    #runs plotter
    HarryPlotter(df, lat_column, lon_column, boundaries, export_path)

if __name__ == "__main__":
    # execute only if run as a script
    main()