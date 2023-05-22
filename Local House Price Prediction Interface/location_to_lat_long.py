import pandas as pd
import googlemaps
import requests

gmaps = googlemaps.Client(key='AIzaSyCeoDaJO26EUzomxAwpDtbaBbEXUBSXpGk')


if __name__ == "__main__":
    df = pd.read_csv("CSV Files/house_price_istanbul.csv", encoding="latin1")

    pd.set_option('display.max_columns', None)
    count = 0
    for index in df.index:
        location = df.at[index, 'location']
        gmaps = googlemaps.Client(key='AIzaSyCeoDaJO26EUzomxAwpDtbaBbEXUBSXpGk')
        try:
            geocode_result = gmaps.geocode(location)
            lat = geocode_result[0]['geometry']['location']['lat']
            lng = geocode_result[0]['geometry']['location']['lng']
            df.at[index, 'lat'] = lat
            df.at[index, 'lng'] = lng
        except:
            print(f"Hatalı String Değeri: {location} + Index: {index}")
        # print(f"Latitude: {lat}")
        # print(f"Longitude: {lng}")
        count += 1
        df_new = df.copy()


    print(count)
    df_new.to_csv( r'C:\Users\furka\OneDrive\Masaüstü\GPII Project\Local House Price Prediction Interface\CSV Files\house_price_istanbul_new.csv')



