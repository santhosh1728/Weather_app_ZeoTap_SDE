# Real-Time Data Processing System for Weather Monitoring

## Objective
The objective of this project is to develop a real-time data processing system for monitoring weather conditions and providing summarized insights using rollups and aggregates. The system utilizes data from the OpenWeatherMap API to deliver comprehensive weather analysis for major Indian metros.

## Features
- **Continuous Data Retrieval:** Automatically fetches weather data from the OpenWeatherMap API at configurable intervals.
- **Data Processing:** Analyzes weather data for major Indian cities, including temperature conversion and condition classification.
- **Daily Summaries:** Generates daily summaries with average, maximum, and minimum temperatures, along with the dominant weather condition.
- **Alerting Mechanism:** Sets thresholds for temperature and specific weather conditions, triggering alerts when these thresholds are breached.
- **Visualizations:** Displays daily summaries, historical trends, and alerts using graphical representations.

## Technologies Used
- **Backend:** Python, Flask
- **Database:** MongoDB
- **Frontend:** HTML, CSS
- **Libraries:** Requests, PyMongo, Matplotlib

## Data Source
The system retrieves weather data from the OpenWeatherMap API. To access the data, you need a free API key, which can be obtained by signing up on the [OpenWeatherMap website](https://openweathermap.org/api). The system focuses on the following weather parameters:
- `main`: Main weather condition (e.g., Rain, Snow, Clear)
- `temp`: Current temperature in Celsius
- `feels_like`: Perceived temperature in Celsius
- `dt`: Time of the data update (Unix timestamp)

## Non-Functional Considerations

### Security
- **API Key Management:** Sensitive information, such as API keys, is stored securely using environment variables to prevent exposure.
- **Data Validation:** Input data is validated at various stages to protect against injection attacks and ensure data integrity.
- **Secure Communication:** The application is designed to support HTTPS to encrypt data transmitted between the client and server.

### Performance
- **Caching:** Implemented caching mechanisms to reduce API call frequency and improve response times.
- **Asynchronous Processing:** Utilized asynchronous programming to handle multiple API requests concurrently, reducing latency.
- **Scalability:** Designed the architecture to handle scaling, enabling the system to manage increased data loads and user traffic efficiently.
- **Database Optimization:** Indexed frequently accessed fields in MongoDB to enhance query performance and reduce response time.

### Monitoring and Logging
- **Logging:** Integrated logging to track application errors, performance metrics, and system events for easier debugging and analysis.
- **Monitoring:** Deployed monitoring tools to observe system performance, uptime, and other critical metrics, ensuring reliable operation.

## Installation

### Prerequisites
- Python 3.6+
- Virtual Environment
- MongoDB

### Setup
1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Required Dependencies:**
   ```bash
   pip install flask requests pymongo matplotlib
   ```

5. **Set up MongoDB:**
   - Ensure MongoDB is running and update the MongoDB connection string in the `config.py` file.

6. **Configure API Key:**
   - Obtain an API key from OpenWeatherMap and update the `config.py` file with your API key.

7. **Store Data:**
   - To store data in MongoDB locally:
     ```bash
     python main.py
     ```

8. **Run the Flask Application:**
   ```bash
   python app.py
   ```

## Usage

### Data Retrieval
The system continuously calls the OpenWeatherMap API at a configurable interval (e.g., every 5 minutes) to retrieve real-time weather data for major Indian metros like Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.

### Data Processing
For each weather update:
- Convert temperature values from Kelvin to Celsius.
- Store the processed data in MongoDB.

### Rollups and Aggregates
**Daily Weather Summary:**
- Calculate and store daily aggregates including:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition

**Alerting Thresholds:**
- Define thresholds for temperature or specific conditions.
- Trigger alerts when thresholds are breached. Alerts can be displayed on the console or sent via email notifications.

### Visualizations
- Display daily weather summaries, historical trends, and triggered alerts.

## Test Cases

### System Setup
- Verify successful startup and connection to the OpenWeatherMap API.

### Data Retrieval
- Simulate API calls at intervals and validate data retrieval and parsing.

### Temperature Conversion
- Test conversion from Kelvin to Celsius.

### Daily Weather Summary
- Simulate weather updates and verify the accuracy of daily summaries.

### Alerting Thresholds
- Test the alerting mechanism by simulating conditions that breach defined thresholds.

## Bonus Features
- **Additional Weather Parameters:** Extend support for parameters like humidity and wind speed in rollups/aggregates.
- **Weather Forecasts:** Implement features for retrieving and summarizing weather forecasts.
