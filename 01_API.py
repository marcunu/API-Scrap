print('Starting the Strava data retrieval program via API')
print('Importing libraries')

#Importing libraries
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import geopy
from geopy.geocoders import Nominatim
import seaborn as sns
import numpy as np

import src.limpieza_texto as lt

import os
from dotenv import load_dotenv
load_dotenv()

print('Libraries imported correctly')

print("Extracting information.")

api_key = os.getenv("token")
url_api = f"https://www.strava.com/api/v3/athlete/activities?access_token={api_key}"
parametros = {"access_token":f"token {api_key}"}
response = requests.get(url = url_api).json()

print("Information  extracted correctly")
print("Creating DataFrame")

#Making a DataFrame with the information.

dicc = {}
actividades = []
for i in range(len(response)):
    print()
    dicc = {
        "Nombre carrera": response[i]['name'],
        "Distancia (km)" : round(response[i]['distance']/1000, 2),
        "Tiempo (min)" : round(response[i]['moving_time']/60,2),
        "Pulso medio (ppm)" : response[i]['average_heartrate'],
        "Altitud (m)" : response[i]['elev_low'],
        "Elevacion (m)" : response[i]['total_elevation_gain'],
        "Fecha" : response[i]['start_date'][:10],
        "Ubicación" : response[i]['start_latlng']
        
    }
    actividades.append(dicc)

    datos = pd.DataFrame(actividades)

#Changing the format from coordenates to the name of the city, state and country

datos['Ciudad'] = datos['Ubicación'].apply(lt.ciudad)
datos['Comunidad Autonoma'] = datos['Ubicación'].apply(lt.comunidad)
datos['Pais'] = datos['Ubicación'].apply(lt.pais)

#Creating new parameters in the DataFrame with the information

datos['Ritmo medio (min/km)'] = round(datos['Tiempo (min)']/datos['Distancia (km)'],2)
datos['Velocidad media (km/h)'] = round(60/datos['Ritmo medio (min/km)'],2)

#sorting the columns to better understand the dataFrame

carreras = datos[['Nombre carrera', 'Distancia (km)', 'Tiempo (min)',
       'Ritmo medio (min/km)', 'Velocidad media (km/h)', 'Pulso medio (ppm)',
       'Altitud (m)', 'Elevacion (m)', 'Fecha', 'Ciudad',
       'Comunidad Autonoma', 'Pais', 'Ubicación']]

#Exporting the information to csv

carreras.to_csv("./data/mis_carreras2.csv")

print("File has been created succesfully")