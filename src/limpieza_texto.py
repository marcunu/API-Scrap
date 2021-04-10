import geopy
from geopy.geocoders import Nominatim


def ciudad(lon_lat):

    '''
    This function returns take the latitude and longitude and returns the name of the city.

    Atributtes:
        -lon_lat: longitude and latitude.

    '''
    coord = lon_lat
    rgeocode = locator.reverse(coord)
    info = rgeocode.raw
    city = info ['address']['city']
    return city

def comunidad(lon_lat):
    '''
    This function returns take the latitude and longitude and returns the name of the state.

    Atributtes:
        -lon_lat: longitude and latitude.
        
    '''    
    coord = lon_lat
    rgeocode = locator.reverse(coord)
    info = rgeocode.raw
    comu = info ['address']['state']
    return comu

def pais(lon_lat):
    
    '''
    This function returns take the latitude and longitude and returns the name of the country.

    Atributtes:
        -lon_lat: longitude and latitude.
        
    '''

    coord = lon_lat
    rgeocode = locator.reverse(coord)
    info = rgeocode.raw
    pais = info ['address']['country']
    return pais