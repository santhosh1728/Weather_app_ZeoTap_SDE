# database.py

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.weather_data

def insert_forecast_data(city, date, temp, humidity, wind_speed, weather_condition):
    db.weather_forecast.insert_one({
        'city': city,
        'date': date.isoformat(),  # Convert date to ISO format string
        'temp': temp,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'weather_condition': weather_condition
    })

def insert_daily_summary(city, date, avg_temp, max_temp, min_temp, avg_humidity, avg_wind_speed, dominant_condition):
    db.daily_weather_summary.insert_one({
        'city': city,
        'date': date,
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'avg_humidity': avg_humidity,
        'avg_wind_speed': avg_wind_speed,
        'dominant_condition': dominant_condition
    })
