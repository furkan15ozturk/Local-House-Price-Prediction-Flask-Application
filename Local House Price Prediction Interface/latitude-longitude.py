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


dataset = pd.read_csv('CSV Files/house_price_istanbul_dataset.csv', encoding='latin1')
dataset.drop('Unnamed: 0.1', axis=1, inplace=True)
dataset.drop('Unnamed: 0', axis=1, inplace=True)
dataset.drop('location', axis=1, inplace=True)
# Print the column names
column_names = dataset.columns
print(column_names)
dataset.to_csv( r'C:\Users\furka\OneDrive\Masaüstü\GPII Project\Local House Price Prediction Interface\CSV Files\house_price_istanbul.csv')
