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

# create basic map
locations_map = Map(location = [my_loc.lat, my_loc.lng],
                height= '100',
                tiles = 'OpenStreetMap', # googlemaps
                zoom_start = 10) # zoom factor
locations_map.add_child(
                Marker(location = [my_loc.lat, my_loc.lng],
                    tooltip = "Mein Standort",
                    icon = folium.Icon(color = 'blue')));

#get_items(file_dict)
def map_add_details(file_dict):
    for i in pd.Series(file_dict):
        name = i['name']
        address = i['address']
        description = i['desc']
        locations = i['location'].split(",")
        year_build = i['year_build']
        directory = i['dir']
        hyperlink_format = '<a href="{link}">{text}</a>'
        hyperlink = hyperlink_format.format(link=directory, text='öffnen')
        folium.features.RegularPolygonMarker(location = [locations[0], locations[1]],
                                                tooltip = name,
                                                popup = "Name:\n" + name
                                                + "\nTyp:\n" + description
                                                + "\nAdresse:\n" + address
                                                + "\nOrdner:\n" + hyperlink
                                                #fill_opacity = 0.8
                                                ).add_to(locations_map)

#map_create_child(my_loc) # build child
map_add_details(file_dict) # add locations into child

locations_map.save("archive_library_map.html") #save html in folder
webbrowser.open("archive_library_map.html", new=2); #open html new tab in webbrowser
