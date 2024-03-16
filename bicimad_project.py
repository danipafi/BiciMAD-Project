#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Para ejecutar este codigo:

# python bicimad_project.py -p
# python bicimad_project.py -o
# python bicimad_project.py -a 


import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Find the nearest BiciMad station')

# Define command-line arguments
parser.add_argument('-p', '--places', action='store_true', help='Generate table for all places of interest')
parser.add_argument('-o', '--origin', type=str, help="Find the nearest station from user's starting point")
parser.add_argument('-a', '--availability', type=str, help="Info about availability of bikes and dockers")

# inicio el parser
parse_args = parser.parse_args()

# variables que le paso por terminal, nombre viene del --nombre
places = parse_args.places
origin = parse_args.origin
availability = parse_args.availability


# Load the results DataFrame from a CSV file
results_df = pd.read_csv('results_df.csv')


# Check which option the user selected and execute the corresponding code
if parse_args.places:
    # Generate table for all places of interest
    pd.set_option('display.max_columns', None)
    print(results_df)

elif parse_args.origin:
    # Filter the results dataframe to only include information about the specified place of interest
    filtered_results_df = results_df[results_df['place_of_interest'] == parse_args.origin]
    pd.set_option('display.max_columns', None)
    print(filtered_results_df)
    
    # Print information about the nearest BiciMAD station
    print(f"Nearest BiciMAD station to {parse_args.origin} is {filtered_results_df['nearest_bicimad_station'].iloc[0]}, located at {filtered_results_df['station_location'].iloc[0]}. Distance: {filtered_results_df['distance'].iloc[0]}.")

elif parse_args.availability:
    # Call the BiciMAD API and print information about bike availability
    import requests as req
    headers = {'email': 'danielebelmiro@gmail.com', 'password': 'Flor2016!'}
    # Realizar la solicitud GET
    emt = req.get('https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/', headers=headers)
    emt.json()
    
    url_bicimad_stations = 'https://openapi.emtmadrid.es/v1/transport/bicimad/stations/'
    access_token = 'b6a8c5fa-ece8-4225-ab5f-6e1953bf5497'
    headers = {
        'accesstoken': access_token}
    stations = req.get(url_bicimad_stations, headers = headers)

    stations

    stations.json()

    import json

    response_data = stations.json()  # Parse the JSON response

    response_data_res = response_data.get('data', [])

    # Crear una lista para almacenar la información relevante
    info_stations = []

    # Iterar a través de cada diccionario en 'data'
    for station in response_data_res:
        station_info = {
            'Nombre de la estación': station.get('name'),
            'Dirección': station.get('address'),
            'Grado de ocupación': station.get('light'),
            'No de bicis disponibles': station.get('dock_bikes'),
            'No de bases libres': station.get('free_bases')
        
        }
        info_stations.append(station_info)

        df_stations_api = pd.DataFrame(info_stations)

    df_stations_api["Grado de ocupación"] = df_stations_api["Grado de ocupación"].apply(lambda x: 'Low' if x == 0 else ('Medium' if x == 1 else ('High' if x == 2 else ('Inactive' if x == 3 else None))))

    df_stations_api.columns = [e.replace(' ', '_').lower() for e in df_stations_api.columns]

    
    bici_station_info = []    


    # Iterate over each row in the DataFrame
    for index, row in df_stations_api.iterrows():
        if row['nombre_de_la_estación'] == parse_args.availability:

            # Get the info of the station
            station_name = row['nombre_de_la_estación']
            station_ocupacion = row['grado_de_ocupación']
            station_bicis_disponibles = row['no_de_bicis_disponibles']
            station_bases_libres = row['no_de_bases_libres']


            # Append the results to the list
            bici_station_info.append({'BiciMAD station': station_name, 'Occupancy level': station_ocupacion, 'Bikes in dockers': station_bicis_disponibles, 'Free dockers': station_bases_libres})

    # Convert the list of dictionaries into a DataFrame
    bici_station_info_df = pd.DataFrame(bici_station_info)

    bici_station_info_df.columns = [e.replace(' ', '_').lower() for e in bici_station_info_df.columns]

    print(bici_station_info_df)


    print(f"{bici_station_info_df['bicimad_station'].iloc[0]}'s occupancy level is {bici_station_info_df['occupancy_level'].iloc[0]} and it has {bici_station_info_df['bikes_in_dockers'].iloc[0]} bikes available and {bici_station_info_df['free_dockers'].iloc[0]} free dockers.")





