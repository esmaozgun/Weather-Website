from flask import Flask,render_template,request
from weatherApp import get_weather_data, convert_to_celc
 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/getWeather", methods=["GET"])
def get_weather():
    api_key = '4814f46b75980f6cfe8d0c3e1108ee27'
    city = request.form.get('city')
    weather_data = get_weather_data(city, api_key)
    if weather_data['cod'] == '404':
        return "No City Found"
    else:
        temperature_fahrenheit = weather_data['main']['temp']
        temperature_celsius = convert_to_celc(temperature_fahrenheit)
        wind_speed = weather_data['wind']['speed']
        wind_direction = weather_data['wind']['deg']
        return render_template("index.html", temperature=temperature_celsius, wind_direction=wind_direction, wind_speed=wind_speed)
    
if __name__ == '__main__':
    app.run(debug=True)