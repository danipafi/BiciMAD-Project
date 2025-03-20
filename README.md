# BiciMAD-Project

Ironhack Madrid - Data Analytics Part Time - Project Module 1

## Description and examples

This is a Python App that allow users to **find the nearest BiciMAD station from all the Municipal Accessible Facilities in Madrid.**

When running the app using argparse, the user has 3 options. They can:

#### 1. Get a table with every Municipal Accessible Facilities in Madrid and their nearest BiciMAD station. It is also available in the [results_df.csv file](https://github.com/danipafi/BiciMAD-Project#:~:text=1%20hour%20ago-,results_df.csv,-Add%20files%20via).

To get the table in the CLI, the user must type "python bicimad_project.py -p" The output will be the following:

| place_of_interest                                     | type_of_place                   | place_address                                         | nearest_bicimad_station                        | station_location                                        | distance    | total_bases |
|-------------------------------------------------------|---------------------------------|-------------------------------------------------------|-----------------------------------------------|---------------------------------------------------------|-------------|-------------|
| Centro de acogida 'Juan Luis Vives'                   | Instalación accesible municipal | CALLE ALCALDE JUAN DE MATA SEVILLANO 18               | 474 - Estación de tren de Vicálvaro          | Calle San Cipriano, 71 ,                                  | 1473 meters | 27          |
| Departamento de Protección a la Infancia y Adolesc... | Instalación accesible municipal | PASEO CHOPERA 41 PLANTA Baja                          | 267 - Paseo de la Chopera - Fernando Poo     | Paseo de la Chopera, 31 ,Comunidad de Madrid Espana,  | 197 meters  | 23          |
| Grupo Municipal Más Madrid                            | Instalación accesible municipal | CALLE MAYOR 71 PLANTA 1ª y 2ª                          | 35 - Plaza del Cordón                        | Plaza del Cordón nº1,                                    | 210 meters  | 24          |
| Grupo Municipal Socialista de Madrid                  | Instalación accesible municipal | CALLE MAYOR 71 PLANTA 3ª y 4ª                          | 35 - Plaza del Cordón                        | Plaza del Cordón nº1,                                    | 210 meters  | 24          |
| Grupo Municipal del Partido Popular                   | Instalación accesible municipal | PLAZA VILLA 5                                          | 9 - Plaza de San Miguel                      | Plaza de San Miguel nº 10,                                | 136 meters  | 24          |
| ...                                                   | ...                             | ...                                                   | ...                                           | ...                                                     | ...         | ...         |
| Área de Gobierno de Economía, Innovación y Hacien... | Instalación accesible municipal | CALLE ALCALA 45                                        | 20A - Banco de España                        | Calle Alcalá nº 48,                                      | 123 meters  | 27          |
| Área de Gobierno de Obras y Equipamientos             | Instalación accesible municipal | CALLE ALCALA 45 PLANTA 3                              | 20A - Banco de España                        | Calle Alcalá nº 48,                                      | 123 meters  | 27          |
| Área de Gobierno de Políticas Sociales, Familias, ... | Instalación accesible municipal | PASEO CHOPERA 41                                       | 267 - Paseo de la Chopera - Fernando Poo     | Paseo de la Chopera, 31 ,Comunidad de Madrid Espana,  | 197 meters  | 23          |
| Área de Gobierno de Urbanismo, Medio Ambiente y M... | Instalación accesible municipal | CALLE RIBERA DEL SENA 21 Edificio Apot. Sede de ...   | 568 - IFEMA A                                | Avenida del Partenón, 6 ,                                  | 192 meters  | 27          |
| Área de Gobierno de Vicealcaldía, Portavoz, Segu... | Instalación accesible municipal | CALLE MONTALBAN 1 PLANTA 5                             | 86 - Cibeles                                 | Paseo del Prado, 1B ,                                     | 145 meters  | 24          |


#### 2. Retrieve the table for a specific place of interest. In this case, the user must type -o and the name of the Municipal Accessible Facility in the CLI. 

Example: python bicimad_project.py -o "Grupo Municipal Más Madrid"

It will generate the following table and print the information in a sentence:  

| place_of_interest           | type_of_place                | place_address              | nearest_bicimad_station | station_location         | distance    | total_bases |
|-----------------------------|------------------------------|----------------------------|-------------------------|--------------------------|-------------|-------------|
| Grupo Municipal Más Madrid | Instalación accesible municipal | CALLE MAYOR 71 PLANTA 1ª y 2ª | 35 - Plaza del Cordón  | Plaza del Cordón nº1, | 210 meters  | 24          |

Nearest BiciMAD station to Grupo Municipal Más Madrid is 35 - Plaza del Cordón, located at Plaza del Cordón nº1,. Distance: 210 meters.

#### 3. Check the availability of bikes and dockers in real time for a specific station.

Example: python bicimad_project.py -a "35 - Plaza del Cordón"

Output: 
| bicimad_station       | occupancy_level | bikes_in_dockers | free_dockers |
|-----------------------|-----------------|------------------|--------------|
| 35 - Plaza del Cordón | High            | 15               | 9            |

35 - Plaza del Cordón's occupancy level is High and it has 15 bikes available and 9 free dockers.


## Core technical concepts

### Main data sources:

#### 1. API REST from [Portal de datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#!/Instalaciones32accesibles32municipales/instalaciones_accesibles_municip_json): /catalogo/202162-0-instalaciones-accesibles-municip.json

The first step was generating a Municipal Accessible Facilities data frame. For that, I called the API, created a loop to iterate through the dictionaries inside the ‘@graph’ key and extract the most important info about the places of interest, and cleaned the dataframe to remove the rows with null values for latitude and longitude.

#### 2. [BiciMAD API](https://apidocs.emtmadrid.es/#api-Block_4_TRANSPORT_BICIMAD) from EMT Madrid

From the BiciMAD API, I retrieved information about all the BiciMAD stations, created a loop to iterate through the dictionaries within the ‘data’ key and extract the most important info about the stations to generate a data frame, and manipulated the data to divide the “Coordinates” column into “Latitude” and “Longitude” and to replace numeric values with words (e. g., “Activa” instead of “1” and “Disponible” instead of 0).


### Script:

To generate the table with all points of interest and their respective nearest BiciMAD station, I imported Geopandas and created functions to transform latitude/longitude data into coordinates in metres and to return the distance between pair points. Then I created a loop to iterate over each place of interest and BiciMAD station, check if the station was active and available and, if so, calculate the distance between points of interest and BiciMAD stations. The 'nearest station' variable was updated whenever a shorter distance was found. The main data frame was subsequently generated and exported as a [CSV file](https://github.com/danipafi/BiciMAD-Project#:~:text=1%20hour%20ago-,results_df.csv,-Add%20files%20via).


To allow users to filter the table by PoI and check bike availability in each station, I created .py file, imported Argparse and defined the command-line arguments and variables. The code includes an if - elif structure to check which of the 3 options the user selected and execute the corresponding code. 



## Main project stack

[Requests](https://requests.readthedocs.io/en/latest/)

[Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

Module geo_calculations.py

[Argparse](https://docs.python.org/3.9/library/argparse.html)

[JSON](https://docs.python.org/3/library/json.html)

