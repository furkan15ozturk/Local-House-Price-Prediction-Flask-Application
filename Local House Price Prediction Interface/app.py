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

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    if request.method == 'POST':
        area_value = int(request.form['area'])
        absolute_area_value = int(request.form['absolute_area'])
        room_value = int(request.form['room'])
        floor_count_value = int(request.form['floor_count'])
        building_age_value = float(request.form['building_age'])
        lat_value, lng_value = get_lat_long(request.form['location'])
        model_value = int(request.form['model'])
        print("lat: ", lat_value, "lng: ", lng_value)

        print("Area:", area_value)
        print("Absolute Area:", absolute_area_value)
        print("Room:", room_value)
        print("Floor Count:", floor_count_value)
        print("Building Age:", building_age_value)
        print("Latitude:", lat_value)
        print("Longitude:", lng_value)
        print("Model:", model_value)

        prediction = model.prediction(area_value, absolute_area_value, room_value, floor_count_value,
                                      building_age_value, lat_value, lng_value, model_value)
        return render_template("index.html", title="İstanbul Ev Fiyat Tahmin Sitesi", price=prediction)
    return render_template("index.html", title="İstanbul Ev Fiyat Tahmin Sitesi")


if __name__ == '__main__':
    app.run()

