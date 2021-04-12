print('Starting the WebScrapin')
print('Importing libraries')

#Importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import src.visualizacion as vt
import numpy as np

print('Libraries imported correctly')

print("Extracting information.")

#Making the webscraping

url_wiki = "https://es.wikipedia.org/wiki/Marat%C3%B3n"
response = requests.get(url_wiki)
soup = BeautifulSoup(response.content, "html.parser")

print("WebScraping complete")
print("Making the DataFrame")

#making the dataframe 

tabla = soup.find_all("table")[1]
rankin_marath = []
rank={}
for f in tabla.find_all("tr"):
    if len(f)>10:
        fila = [e for e in f.find_all("td")]
        if len(fila) > 0:
            rank = {
                "Posicion" : fila[0].text.strip(),
                "Tiempo" : fila[1].text.strip(),
                "Nombre" : fila[2].text.strip(),
                "Pais" : fila[3].find("a").text.strip(),
                "Fecha" : fila[4].text.strip(),
                "Lugar": fila[5].text.strip()
            }

        rankin_marath.append(rank)

corredores = pd.DataFrame(rankin_marath)

#change time format 

corredores['Tiempo (min)'] = corredores['Tiempo'].apply(vt.cambio_minutos)


#Creating new parameters

corredores['Ritmo (min/km)'] = round(corredores ['Tiempo (min)']/42.2, 2)
corredores['Velocidad media (km/h)'] = round(60/corredores['Ritmo (min/km)'],2)

#Separating men from women

hombres = corredores.drop([0, 11, 12, 13, 14 , 15, 16, 17, 18, 19, 20, 21], axis = 0).set_index('Posicion')
mujeres = corredores.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], axis = 0).set_index('Posicion')

#Exporting files
print("Exporting files")

hombres.to_csv("./data/marath_hombres2.csv")
mujeres.to_csv("./data/marath_mujeres2.csv")

print("Files exported correctly")

