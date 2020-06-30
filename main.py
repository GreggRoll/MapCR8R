from GUI import input_sg
import plotter
import PySimpleGUI as sg

def main():
    inputs = input_sg()
    #shape files return 5 while lat/long return 8
    if len(inputs) == 5:
        df, geometry_type, plot_col, boundaries, export_path = inputs
        print(inputs)
        #popup reads data input back to you
        sg.popup('Results', "DataFrame head: ",df.head(), "Plot column :"+str(plot_col), "Boundaries :"+str(boundaries),"export path: "+export_path)
        plotter.shp_plotter(df, plot_col,boundaries, export_path)
    #lat/Long
    else:
        print(inputs)
        df, geometry_type, lat_column, lon_column, plot_col, boundaries, export_path, plot_type = inputs
        sg.popup('Results', "DataFrame head: ",df.head(), "Lat: "+lat_column, "Long: "+lon_column, "Plot column :"+str(plot_col), "Boundaries :"+str(boundaries),"export path: "+export_path, "Plot type : "+plot_type)
        plotter.lat_lon_plotter(df, lat_column, lon_column, plot_col, boundaries, export_path, plot_type)

if __name__ == "__main__":
    # execute only if run as a script
    main()