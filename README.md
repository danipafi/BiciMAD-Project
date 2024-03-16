# BiciMAD-Project
This is a Python App that allow users to find the nearest BiciMAD station from all the Municipal Accessible Facilities in Madrid.

When executing the app using argparse, the user has 3 options. They can:

1. Get a table with every Municipal Accessible Facilities in Madrid and their nearest BiciMAD station. It is also available in the results_df.csv file.

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


2. Get the table for a specific place of interest. In this case, the user must type -o and the name of the Municipal Accessible Facility in the CLI. 

Example: python bicimad_project.py -o "Grupo Municipal Más Madrid"

It will generate the following table and print this info in a sentence:  

| place_of_interest           | type_of_place                | place_address              | nearest_bicimad_station | station_location         | distance    | total_bases |
|-----------------------------|------------------------------|----------------------------|-------------------------|--------------------------|-------------|-------------|
| Grupo Municipal Más Madrid | Instalación accesible municipal | CALLE MAYOR 71 PLANTA 1ª y 2ª | 35 - Plaza del Cordón  | Plaza del Cordón nº1, | 210 meters  | 24          |

Nearest BiciMAD station to Grupo Municipal Más Madrid is 35 - Plaza del Cordón, located at Plaza del Cordón nº1,. Distance: 210 meters.

3. Check the availability of bikes and dockers in real time for a specific station.
Example: python bicimad_project.py -a "35 - Plaza del Cordón"

Output: 
| bicimad_station       | occupancy_level | bikes_in_dockers | free_dockers |
|-----------------------|-----------------|------------------|--------------|
| 35 - Plaza del Cordón | High            | 15               | 9            |

35 - Plaza del Cordón's occupancy level is High and it has 15 bikes available and 9 free dockers.
