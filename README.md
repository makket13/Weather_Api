Weather Forecast API

This project fetches weather forecasts from the Meteomatics API and stores them in an SQLite database. Additionally, a Flask-based API is provided to retrieve the latest weather data and perform various calculations.

Features

Fetches weather data for 3 different locations and stores the data in an SQLite database.
Provides API endpoints to:

List the latest forecast for each location for every day.
Calculate the average temperature of the last 3 forecasts for each location.
Get the top n locations based on a specified weather metric.


Setup Instructions


1. Install Dependencies
Ensure you have Python installed on your system. You can install the required dependencies by running the following command in your terminal:

pip install -r requirements.txt


2. Fetch Weather Data
To fetch the weather data for 3 different locations and store them in the SQLite database, run:

python weather_fetcher.py

This script retrieves the weather forecasts from the Meteomatics API and stores the data (temperature, precipitation, wind speed) for the specified locations in the weather.db database.


3. Run the Flask API
Once the weather data is stored in the SQLite database, you can start the Flask API to serve the weather data. Run the following command:

python app.py

The API will be available at http://127.0.0.1:5000/.


API Endpoints

/locations: Lists the latest weather data (temperature, precipitation, wind speed) for each location.

/average_temp: Lists the average temperature of the last 3 forecasts for each location.

/top_locations?n=<number>: Returns the top n locations based on a specific metric (temperature, 
precipitation, or wind speed). The n parameter specifies how many top locations you want to retrieve.


Example API Requests
1. Get the latest forecast for all locations:

curl http://127.0.0.1:5000/locations


2. Get the average temperature of the last 3 forecasts:

curl http://127.0.0.1:5000/average_temp


3. Get the top 3 locations based on temperature:

curl http://127.0.0.1:5000/top_locations?n=3



Example Response:

[
    ["Berlin", "2024-09-08T00:00:00Z", 22.6, 0.0, 3.7],
    ["London", "2024-09-08T00:00:00Z", 15.4, 0.1, 2.5]
]



Dependencies

Python 3.x
Flask 3.0.3
requests 2.27.1

Make sure that you install the correct versions of these dependencies using the requirements.txt file.

License

This project is licensed under the MIT License.