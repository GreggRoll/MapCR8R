from GUI import input_sg
import plotter
import PySimpleGUI as sg

def main():
    inputs = input_sg()
    #shape files return 5 while lat/long return 8
    if len(inputs) == 6:
        df, geometry_type, plot_col, boundaries, export_path, legend = inputs
        print(inputs)
        #popup reads data input back to you
        sg.popup('Results', "Geometry type: "+geometry_type, "DataFrame head: ",df.head(), "Plot column :"+str(plot_col), "Boundaries :"+str(boundaries),"export path: "+export_path)
        plotter.shp_plotter(df, plot_col,boundaries, export_path, legend)
    #lat/Long
    else:
        print(inputs)
        df, geometry_type, lat_column, lon_column, plot_col, boundaries, export_path, plot_type, legend = inputs
        sg.popup('Results',  "Geometry type: "+geometry_type, "DataFrame head: ",df.head(), "Lat: "+lat_column, "Long: "+lon_column, "Plot column :"+str(plot_col), "Boundaries :"+str(boundaries),"export path: "+export_path, "Plot type : "+plot_type)
        plotter.lat_lon_plotter(df, lat_column, lon_column, plot_col, boundaries, export_path, plot_type, legend)

if __name__ == "__main__":
    # execute only if run as a script
    main()