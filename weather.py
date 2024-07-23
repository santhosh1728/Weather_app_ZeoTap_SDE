# weather.py

import requests
import datetime as dt
from config import API_KEY, CITIES, BASEURL, FORECASTURL, THRESHOLD_TEMP
from database import insert_forecast_data, insert_daily_summary
from email_alerts import send_email_alert

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit

def fetch_and_process_weather_data():
    daily_data = {city: {'temps': [], 'humidities': [], 'wind_speeds': [], 'conditions': []} for city in CITIES}

    for city in CITIES:
        print(f"Processing city: {city}")
        
        # Fetch current weather
        url = f"{BASEURL}?q={city}&appid={API_KEY}"
        response = requests.get(url).json()

        # Ensure the response is valid
        if 'main' not in response or 'weather' not in response or 'wind' not in response:
            print(f"Error fetching data for {city}: {response}")
            continue

        temp_kelvin = response['main']['temp']
        temp_celsius, _ = kelvin_to_celsius_fahrenheit(temp_kelvin)
        humidity = response['main']['humidity']
        wind_speed = response['wind']['speed']
        description = response['weather'][0]['description']
        sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

        print(f"Temperature in {city}: {temp_celsius:.2f}°C")
        print(f"Humidity in {city}: {humidity}%")
        print(f"Wind speed in {city}: {wind_speed} m/s")
        print(f"General weather in {city}: {description}")
        print(f"Sunrise in {city} at {sunrise_time} local time.")
        print(f"Sunset in {city} at {sunset_time} local time.")
        print("\n")

        # Append data for daily summary
        daily_data[city]['temps'].append(temp_celsius)
        daily_data[city]['humidities'].append(humidity)
        daily_data[city]['wind_speeds'].append(wind_speed)
        daily_data[city]['conditions'].append(description)

        # Check for alerting conditions
        if temp_celsius > THRESHOLD_TEMP:
            send_email_alert(city, description, temp_celsius)

        # Fetch and store forecast data
        forecast_url = f"{FORECASTURL}?q={city}&appid={API_KEY}"
        forecast_response = requests.get(forecast_url).json()

        # Ensure the forecast response is valid
        if 'list' not in forecast_response:
            print(f"Error fetching forecast data for {city}: {forecast_response}")
            continue

        print(f"Fetching forecast data for {city}")
        for entry in forecast_response['list']:
            forecast_temp_kelvin = entry['main']['temp']
            forecast_temp_celsius, _ = kelvin_to_celsius_fahrenheit(forecast_temp_kelvin)
            forecast_humidity = entry['main']['humidity']
            forecast_wind_speed = entry['wind']['speed']
            forecast_condition = entry['weather'][0]['description']
            forecast_date = dt.datetime.fromtimestamp(entry['dt']).date()

            print(f"Inserting forecast data for {city} on {forecast_date}")
            # Insert forecast data
            insert_forecast_data(city, forecast_date, forecast_temp_celsius, forecast_humidity, forecast_wind_speed, forecast_condition)

    # Calculate and store daily summaries
    for city, data in daily_data.items():
        if not data['temps']:
            continue
        avg_temp = sum(data['temps']) / len(data['temps'])
        max_temp = max(data['temps'])
        min_temp = min(data['temps'])
        avg_humidity = sum(data['humidities']) / len(data['humidities'])
        avg_wind_speed = sum(data['wind_speeds']) / len(data['wind_speeds'])
        conditions = data['conditions']
        dominant_condition = max(set(conditions), key=conditions.count)  # Simplistic dominant condition calculation

        today = dt.datetime.now().strftime('%Y-%m-%d')
        print(f"Inserting daily summary for {city} on {today}")
        insert_daily_summary(city, today, avg_temp, max_temp, min_temp, avg_humidity, avg_wind_speed, dominant_condition)
