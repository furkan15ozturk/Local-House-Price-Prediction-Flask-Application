import googlemaps
from datetime import datetime
import unicodedata
import pandas as pd


gmaps = googlemaps.Client(key='AIzaSyCeoDaJO26EUzomxAwpDtbaBbEXUBSXpGk')

def lat_lng_converter(address):
    geocode_result = gmaps.geocode('address')

    location = geocode_result[0]['geometry']['location']

    lat = location['lat']
    lng = location['lng']

    print(f"Latitude: {lat}")
    print(f"Longitude: {lng}")

    return lat, lng



