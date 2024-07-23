# config.py

API_KEY = open('apikey.txt', 'r').read().strip()  # Reading API key from a file named 'apikey.txt'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
BASEURL = "https://api.openweathermap.org/data/2.5/weather"
FORECASTURL = "https://api.openweathermap.org/data/2.5/forecast"
INTERVAL = 5 * 60  # 5 minutes in seconds
THRESHOLD_TEMP = 35  # Example threshold temperature in Celsius
