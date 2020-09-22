# Archive-Mapping
Mapping of geo-located archive files

Inspired by the idea of having a bundle of old archived plots and maps you want to have digital.

# Proceeding
0. At first the map description (name, adress, location,...) has to be read (OCR) from the map and saved as JSON-file (.txt) inside the folder
required format for this script:
dict:
{
  'name': "some name",
  'type': 'my type',
  'adress': 'my adress (optional)',
  'desc': "some description",
  'year_build': year of construction,
  'location': 'latitude, longitude'
}

example:

{
  "name": "Regenbecken-4",
  "type": "Speicher",
  "adress": "Auggen, 79424, Germany",
  "desc": "Becken",
  "year_build": 1700,
  "location": "47.790770, 7.583286"}


1. A file crawler searches for specific files and collects them
2. Locations are mapped in a interactive GUI
