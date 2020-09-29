# Archive-Mapping
Mapping of geo-located,  archive files and schemes.

Inspired by the idea of having a bundle of old archived schemes and plots from infrastructural buildings that have to be digitalized and mapped in a clear way.

# Proceeding
## file structure requirements
At first the map description (name, adress, location,...) has to be read (OCR) from the scheme and saved as JSON-file (.xml). Each building with it's schemes should be  inside an individual folder. Required format for this location file saved as "location.xml" (dictionary):


    {
    "name": "some name",
    "type": 'my type',
    "adress": 'my adress (optional)',
    "desc": "some description",
    "year_build": year of construction,
    "location": 'latitude, longitude'
    }

example:

`{"name": "Regenbecken-4",
"type": "Speicher",
"adress": "Auggen, 79424, Germany",
"desc": "Becken",
"year_build": 1700,
"location": "47.790770, 7.583286"}`

the folder structure should look like:
>
>location1
>* file1
>* loction.xml
>
>location2
>* file2
>* location.xml
>
> ...

## run program
Save the "mapping-locations.py" in your schemes root folder. A file crawler will search for the specific loacation.xml files and collect them. The locations are than mapped in your local standard browser and a Excel file "locations_collection.xml" is saved in your schemes root folder.

# Requirements
The python libraries from "python_environment.yml" should be installed locally.