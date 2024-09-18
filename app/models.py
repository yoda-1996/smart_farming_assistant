import sqlite3
import requests

def get_weather_data(city):
    api_key = '18f6cb7499383f31e9987ea68d7ff8d4' 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def init_db():
    conn = sqlite3.connect('farming.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS crops 
                 (id INTEGER PRIMARY KEY, name TEXT, water_schedule TEXT)''')
    conn.commit()
    conn.close()
