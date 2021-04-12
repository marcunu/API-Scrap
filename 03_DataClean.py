print("Cleaning data from original dataset")
print("Importing libraies")

import pandas as pd
import src.limpieza_texto as lt
import src.visualizacion as vt

print("Libraries Imported")


#Import DataFrame
print("Importing DataFrame")

hkm = pd.read_csv("data/challenge.csv")

#Cleaning DataFrame
print("Cleaning DataFrame")
hkm['Tiempo (min)'] = hkm['Official Time'].apply(vt.cambio_minutos)
hkm['Ritmo (min/km)'] = round(hkm['Tiempo (min)']/42.2, 2)
hkm['Velocidad media (km/h)'] = round(60/hkm['Ritmo (min/km)'],2)


hkm1 = hkm.head(100)
hkm2 = hkm.head(900)
hkm3 = hkm2.tail(100)


#Exporting DataFrame
print("Exporting dataFrame")

hkm1.to_csv("./data/top_100.csv")
hkm3.to_csv("./data/average.csv")

print("Data cleaning is complete!")
