# weather.py

import requests
import datetime as dt
from config import API_KEYS, CITIES, BASEURL, FORECASTURL, THRESHOLD_TEMP
from database import insert_forecast_data, insert_daily_summary
from email_alerts import send_email_alert

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit

def fetch_weather_data(city):
    data = {}
    for api_key in API_KEYS:
        response = requests.get(f"{BASEURL}?q={city}&appid={api_key}")
        if response.status_code == 200:
            data[api_key] = response.json()
    return data

def fetch_and_process_weather_data():
    daily_data = {city: {'temps': [], 'humidities': [], 'wind_speeds': [], 'conditions': []} for city in CITIES}

    for city in CITIES:
        print(f"Processing city: {city}")
        
        # Fetch current weather
        response = fetch_weather_data(city)

        # Ensure the response is valid
        if not response:
            print(f"Error fetching data for {city}")
            continue
        
        for api_key, weather_data in response.items():
            if 'main' not in weather_data or 'weather' not in weather_data or 'wind' not in weather_data:
                print(f"Error fetching data for {city} from API key {api_key}")
                continue

            temp_kelvin = weather_data['main']['temp']
            temp_celsius, _ = kelvin_to_celsius_fahrenheit(temp_kelvin)
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            description = weather_data['weather'][0]['description']
            sunrise_time = dt.datetime.utcfromtimestamp(weather_data['sys']['sunrise'] + weather_data['timezone'])
            sunset_time = dt.datetime.utcfromtimestamp(weather_data['sys']['sunset'] + weather_data['timezone'])

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
            forecast_url = f"{FORECASTURL}?q={city}&appid={API_KEYS[0]}"  # Using the first API key for simplicity
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
