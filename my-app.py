import json
import requests
from flask import jsonify
from flask import Flask
app = Flask(__name__)


api_key = 'be8d3e323de722ff78208a7dbb2dcd6f'
api_url = 'http://api.openweathermap.org/data/2.5/forecast/daily'

# For temperature in Celsius use "metric", For temperature in Fahrenheit use "imperial"
unit = 'metric'
# number of days do you want to get data
number_of_days = 14


@app.route('/<city_name>')
def get_weather_json(city_name):
    params = {
        'q': city_name,
        'cnt': number_of_days,
        'appid': api_key,
        'units': unit
    }
    data_weather_response = requests.get(api_url, params=params).json()
    return jsonify(data_weather_response)
