## Map CR8R
This project is intended to allow users to quickly be able to plot data. 

feature demo July 8 2020
[![Watch the video](images/demo.png)](https://drive.google.com/file/d/1WySkLcwzDR5q21vISP0OW17lb4qQzfQ-/view)

# supported features

# Sample Plot Map
![demo map](images/plot_map.png)
Plots points on map in given bounds using a lat/long column.
# Sample 3D Heat Map
![Heat Map](images/3D_HM.png)
Creates a kdeplot fitting and plotting a univariate kernel density estimate.
# Sample Shape plot map
![Shape Map](images/Shape_plot_map.png)
Plots a shapefile onto a map in given bounds, optionally plots a column and provides a legend if selected.
# Sample shape generator
![American shapes](images/Shape_Generator.png)
Product of shape_generator.py. Allows users to create n number of shapes with random locations in x,y,x1,y1 bounds.

# Requirements
- PySimpleGUI
- geopandas
- pandas
- cartopy.crs
- cartopy
- matplotlib.pyplot
