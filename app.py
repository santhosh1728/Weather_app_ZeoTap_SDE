from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual OpenWeatherMap API key
API_KEY = open('apikey.txt', 'r').read().strip()  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400
    
    # Fetch current weather
    weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
    if weather_response.status_code != 200:
        return jsonify({'error': f'Error fetching weather data: {weather_response.status_code} {weather_response.reason}'}), weather_response.status_code
    
    weather_data = weather_response.json()
    temp = weather_data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
    weather_description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    # Fetch 5-day forecast
    forecast_response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}')
    if forecast_response.status_code != 200:
        return jsonify({'error': f'Error fetching forecast data: {forecast_response.status_code} {forecast_response.reason}'}), forecast_response.status_code
    
    forecast_data = forecast_response.json()
    forecast_list = forecast_data['list']
    forecast_summary = []
    for entry in forecast_list[:5]:  # Get forecast for the next 5 intervals (3-hour intervals)
        date = entry['dt_txt']
        temp = entry['main']['temp'] - 273.15
        description = entry['weather'][0]['description']
        forecast_summary.append({
            'date': date,
            'temperature': round(temp, 2),
            'description': description
        })

    return jsonify({
        'city': city,
        'current': {
            'temperature': round(temp, 2),
            'description': weather_description,
            'humidity': humidity,
            'wind_speed': wind_speed
        },
        'forecast': forecast_summary
    })

if __name__ == '__main__':
    app.run(debug=True)
