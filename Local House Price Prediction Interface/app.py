from flask import Flask, render_template, request
import model
import googlemaps

app = Flask(__name__)

gmaps = googlemaps.Client(key='AIzaSyCeoDaJO26EUzomxAwpDtbaBbEXUBSXpGk')

def get_lat_long(address):
    geocode_result = gmaps.geocode(address)
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lng = geocode_result[0]["geometry"]["location"]["lng"]
    return lat, lng
@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    if request.method == 'POST':
        area_value = int(request.form['area'])
        absolute_area_value = int(request.form['absolute_area'])
        room_value = int(request.form['room'])
        floor_count_value = int(request.form['floor_count'])
        building_age_value = int(request.form['building_age'])
        lat_value, lng_value = get_lat_long(request.form['location'])
        print("lat: ", lat_value, "lng: ", lng_value)
        prediction = model.prediction(area_value, absolute_area_value, room_value, floor_count_value,
                                      building_age_value, lat_value, lng_value)
        return render_template("index.html", title="İstanbul Ev Fiyat Tahmin Sitesi", price=prediction)
    return render_template("index.html", title="İstanbul Ev Fiyat Tahmin Sitesi")


if __name__ == '__main__':
    app.run()
