# main.py

import time
from weather import fetch_and_process_weather_data
from plotting import plot_daily_summaries
from config import INTERVAL
from email_alerts import send_email_alert

if __name__ == '__main__':
    while True:
        fetch_and_process_weather_data()
        time.sleep(INTERVAL)
