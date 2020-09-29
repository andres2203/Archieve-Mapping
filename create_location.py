import pandas as pd
import json

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
