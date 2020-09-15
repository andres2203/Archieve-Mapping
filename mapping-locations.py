import json, string
import folium
#import requests
import geocoder
#import pandas as pd
import matplotlib
import numpy as np
import pandas as pd
import os
import webbrowser
from folium import Map, Marker#, GeoJson, LayerControl
#from ediblepickle import checkpoint

path_root = os.getcwd()
path = os.path.join(path_root, 'data/') # Import specific directory
file_dict = []
path_list = []
# function to walk through dirs and collect "location.txt" files
def file_reader(path):
    for root, dirs, files in os.walk(path): # searches in folders, subfolders and files
        for name in dirs:
            file_path = os.path.join(root, name)
            for txt_file in os.listdir(file_path):

                if txt_file == 'location.txt':
                    file = os.path.join(file_path, txt_file) # get filepath for each file
                    path_list.append(file)

                    with open(file) as json_file: # collect json contend
                        data = json.load(json_file)
                        file_path = file_path+"/"
                        #print(file_path)
                        data.update({"dir" : file_path})
                        file_dict.append(data) # append json dict to file_dict
file_reader(path)
# Mapping of files
my_loc = geocoder.ip('me') # get my loction
locations_map = Map(location = [my_loc.lat, my_loc.lng],
                    height= '100',
                    tiles = 'OpenStreetMap',
                    zoom_start = 8)

locations_map.add_child(
   Marker(location = [my_loc.lat, my_loc.lng],
                      tooltip = "Mein Standort",
                      icon = folium.Icon(color = 'blue')));

# Mapping of all data
for i in pd.Series(file_dict):
    name = i['name']
    address = i['adress']
    description = i['desc']
    locations = i['location'].split(",")
    year_build = i['year_build']
    folium.features.RegularPolygonMarker(location = [locations[0], locations[1]],
                                        tooltip = name,
                                        popup = "Name:\n" + name
                                        + "\nTyp:\n" + description
                                        + "\nAdresse:\n" + address
                                        + "\nPath:\n" + ('<a href="/home/andres/DataScience/Archive-Mapping/data/test 6">open dir</a>'),
                                        fill_opacity = 0.8
                                        ).add_to(locations_map)
# opens result in browser
locations_map.save("locations_map.html")
webbrowser.open("locations_map.html", new=2); #open new tab in webbrowser
