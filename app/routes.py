from flask import render_template, request
from app import app
import requests
from app.models import get_weather_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    data = get_weather_data(city)
    return render_template('index.html', weather=data, city=city)
