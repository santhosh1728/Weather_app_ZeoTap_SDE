# Real-Time Data Processing System for Weather Monitoring

# Objective
Develop a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system utilizes data from the OpenWeatherMap API.

# Features

-> Continuous retrieval of -> weather data from the OpenWeatherMap API.
-> Processing and analysis of weather data for major Indian metros.
-> Daily weather summaries including average, maximum, and minimum temperatures, and dominant weather conditions.
-> Alerting thresholds for temperature and specific weather conditions.
-> Visualizations for daily 
summaries, historical trends, and triggered alerts.


# Technologies Used

-> Python
-> Flask
-> MongoDB
-> HTML
-> Css


# Data Source

The system retrieves weather data from the OpenWeatherMap API. You need to sign up for a free API key to access the data. The API provides various weather parameters, and for this assignment, we focus on:

-> main: Main weather condition (e.g., Rain, Snow, Clear)
-> temp: Current temperature in Celsius
-> feels_like: Perceived temperature in Celsius
-> dt: Time of the data update (Unix timestamp)

# Installation
* Prerequisites

-> Python 3.6+
-> Virtual Environment
-> MongoDB

# Setup

1. Clone the repository:

git clone <repository-url>
cd <repository-directory>

2. Create a virtual environment:

python -m venv venv

3. Activate the virtual environment:

-> On Windows:

venv\Scripts\activate


-> On macOs/Linux:

source venv/bin/activate

4. Install the required dependencies:

pip install -r requirements.txt


5. Set up MongoDB and ensure it is running. Update the MongoDB connection string in the config.py file.


6. Obtain an API key from OpenWeatherMap and update the config.py file with your API key.

7. Run the Flask application:

python app.py


# Usage
* Data Retrieval

The system continuously calls the OpenWeatherMap API at a configurable interval (e.g., every 5 minutes) to retrieve real-time weather data for the metros in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).

* Data Processing
For each received weather update:

-> Convert temperature values from Kelvin to Celsius.
-> Store the weather data in MongoDB.

* Rollups and Aggregates
1. Daily Weather Summary:

-> Roll up the weather data for each day.
-> Calculate daily aggregates for:
    -> Average temperature
    -> Maximum temperature  
    -> Minimum temperature
    -> Dominant weather condition
-> Store the daily summaries in MongoDB for further analysis.

2. Alerting Thresholds:

-> Define user-configurable thresholds for temperature or specific weather conditions (e.g., alert if temperature exceeds 35 degrees Celsius for two consecutive updates).
-> Continuously track the latest weather data and compare it with the thresholds.
-> Trigger an alert if a threshold is breached. Alerts can be displayed on the console or sent through an email notification system.


3. Visualizations:

->Display daily weather summaries, historical trends, and triggered alerts.


# Test Cases
1. System Setup:

-> Verify the system starts successfully and connects to the OpenWeatherMap API using a valid API key.

2. Data Retrieval:

-> Simulate API calls at configurable intervals.
-> Ensure the system retrieves weather data for the specified location and parses the response correctly.

3. Temperature Conversion:

-> Test conversion of temperature values from Kelvin to Celsius based on user preference.

4. Daily Weather Summary:

-> Simulate a sequence of weather updates for several days.
-> Verify that daily summaries are calculated correctly, including average, maximum, minimum temperatures, and dominant weather condition

5. Alerting Thresholds:

-> Define and configure user thresholds for temperature or weather conditions.
-> Simulate weather data exceeding or breaching the thresholds.
-> Verify that alerts are triggered only when a threshold is violated.


# Bonus Features

-> Extend the system to support additional weather parameters from the OpenWeatherMap API (e.g., humidity, wind speed) and incorporate them into rollups/aggregates.
-> Explore functionalities like weather forecasts retrieval and generating summaries based on predicted conditions.

