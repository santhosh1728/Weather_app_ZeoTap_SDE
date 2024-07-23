# plotting.py

import matplotlib.pyplot as plt
from database import db

def plot_daily_summaries():
    data = list(db.daily_weather_summary.find())
    
    cities = set(row['city'] for row in data)
    for city in cities:
        city_data = [row for row in data if row['city'] == city]
        dates = [row['date'] for row in city_data]
        avg_temps = [row['avg_temp'] for row in city_data]
        
        plt.plot(dates, avg_temps, label=f'{city} Avg Temp')
    
    plt.xlabel('Date')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Daily Average Temperature')
    plt.legend()
    plt.show()
