import json, string

#Folium uses the Leaflet API to allow users to write Python code to generate and manipulate interactive JavaScript maps. This also allows for drawing those maps in Jupyter notebooks
import folium
#import requests
import geocoder
#import pandas as pd
import matplotlib
import numpy as np
import pandas as pd
import os
import webbrowser
from folium import Map, Marker, Popup#, GeoJson, LayerControl
#from ediblepickle import checkpoint


get_ipython().run_line_magic("matplotlib", " inline ")


get_ipython().getoutput("conda info # basic info about env")


# for testing purpose generated json files


building_name = input('Location name ')
building_type = input('Building type ')
address = input('location address ')
building_desc = input('some further description ')
year = pd.to_numeric(input('year of construction '))
latitude = input('coordinates for latitude ')
longitude = input('coordinates for longitude ')

data = {
    'name': building_name,
    'type': building_type,
    'address': address,
    'desc': building_desc,
    'year_build': year,
    'location': latitude + ',' + longitude
}

with open('location.xml', 'w') as outfile:
    json.dump(data, outfile)


path_root = os.getcwd()
path = os.path.join(path_root, 'data/')  # Import specific directory
file_dict = []
path_list = []


file_dict = []
path_list = []

# function to walk through dirs and collect "location.txt" files
def file_reader(my_path):
    for root, dirs, files in os.walk(my_path):  # searches in folders, sub folder and files
        for name in dirs:
            file_path = os.path.join(root, name)
            for txt_file in os.listdir(file_path):

                if txt_file == 'location.xml':
                    file = os.path.join(file_path, txt_file)  # get filepath for each file
                    path_list.append(file)

                    with open(file) as json_file:  # collect json contend
                        data = json.load(json_file)
                        file_path = file_path + "/"  # to get in next dir
                        data.update({"dir": file_path})
                        file_dict.append(data)  # append json dict to file_dict



file_reader(path)


# get my loction
my_loc = geocoder.ip('me')


locations_map = Map(location = [my_loc.lat, my_loc.lng],
                    height= '100',
                    tiles = 'OpenStreetMap',
                    zoom_start = 8)
locations_map.add_child(
   Marker(location = [my_loc.lat, my_loc.lng],
                      tooltip = "Mein Standort",
                      icon = folium.Icon(color = 'blue')));


def map_add_details(data):
    for i in pd.Series(data):
        name = i['name']
        address = i['address']
        description = i['desc']
        building_location = i['location'].split(",")
        year_build = i['year_build']
        directory = i['dir']
        hyperlink_format = '<a href="{link}">{text}</a>'  # format for hyperlinks
        hyperlink = hyperlink_format.format(link=directory, text='öffnen')  # to get individual hyperlinks
        folium.features.RegularPolygonMarker(location=[building_location[0], building_location[1]],
                                             tooltip=name,
                                             popup="Name:\n" + name
                                             + "\nTyp:\n" + description
                                             + "\nAdresse:\n" + address
                                             + "\nBaujahr:\n" + str(year_build)
                                             + "\nOrdner:\n" + hyperlink
                                            ).add_to(locations_map)


map_add_details(file_dict)  # add locations into child
locations_map.save("locations_collection_map.html")  # save html in folder
webbrowser.open("locations_collection_map.html", new=2)  # open html new tab in br


import kivy;




import cgitb
cgitb.enable()

print("Content-Type: text/plain;charset=utf-8")
print

print("hello world")
