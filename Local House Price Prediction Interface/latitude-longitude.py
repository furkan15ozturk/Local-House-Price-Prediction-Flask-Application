import googlemaps
from datetime import datetime
import unicodedata
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyCeoDaJO26EUzomxAwpDtbaBbEXUBSXpGk')

geocode_result = gmaps.geocode('Istanbul - Çekmekoy - Güngoren Mahallesi')

location = geocode_result[0]['geometry']['location']

lat = location['lat']
lng = location['lng']

print(f"Latitude: {lat}")
print(f"Longitude: {lng}")


def contains_non_latin(word):
    for char in word:
        if unicodedata.category(char)[0] != 'L':
            return True
    return False

dataset = pd.read_csv('house_price_istanbul.csv', encoding='latin1')
column_data = dataset['location']
non_latin_words = [word for word in column_data if contains_non_latin(word)]
print(non_latin_words)

