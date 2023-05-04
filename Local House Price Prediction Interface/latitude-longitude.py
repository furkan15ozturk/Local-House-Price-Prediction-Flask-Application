import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCeoDaJO26EUzomxAwpDtbaBbEXUBSXpGk')

geocode_result = gmaps.geocode('İstanbul - Arnavutköy - Anadolu Mahallesi')

location = geocode_result[0]['geometry']['location']

lat = location['lat']
lng = location['lng']

print(f"Latitude: {lat}")
print(f"Longitude: {lng}")
