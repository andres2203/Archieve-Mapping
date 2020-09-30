import json
import os
import webbrowser

import folium
import geocoder
import pandas as pd
from folium import Map, Marker

path_root = os.getcwd()
path = os.path.join(path_root, 'data/')  # Import specific directory
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


file_reader(path)  # run function with path

df = pd.DataFrame(file_dict)  # create a DataFrame from list
df.to_excel("locations_collection.xlsx", index=False)  # save df as Excel file
df.to_csv('locations_collection.csv', index=False)  # save df as CSV file

my_loc = geocoder.ip('me')  # get my location

# create basic map
locations_map = Map(location=[my_loc.lat, my_loc.lng],
                    height='100',
                    tiles='OpenStreetMap',  # loads map from open street maps
                    zoom_start=10)  # zoom factor
locations_map.add_child(
    Marker(location=[my_loc.lat, my_loc.lng],
           tooltip="Mein Standort",
           icon=folium.Icon(color='blue'))
)


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
                                                   + "\nBaujahr\n" + str(year_build)
                                                   + "\nOrdner:\n" + hyperlink
                                             ).add_to(locations_map)


map_add_details(file_dict)  # add locations into child
locations_map.save("locations_collection_map.html")  # save html in folder
webbrowser.open("locations_collection_map.html", new=2)  # open html new tab in browser
