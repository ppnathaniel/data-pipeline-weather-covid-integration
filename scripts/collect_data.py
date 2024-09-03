import os
import requests
import json
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
weather_api_key = os.getenv('WEATHER_API_KEY')

# Collect weather data from OpenWeatherMap API
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={weather_api_key}"

weather_response = requests.get(weather_url)
weather_data = weather_response.json()

# Collect COVID-19 data from COVID-19 Data API
covid_url = "https://disease.sh/v3/covid-19/all"
covid_response = requests.get(covid_url)
covid_data = covid_response.json()

# Save data locally as JSON files
with open('data/weather_data.json', 'w') as f:
    json.dump(weather_data, f)

with open('data/covid_data.json', 'w') as f:
    json.dump(covid_data, f)

# Convert JSON to DataFrame and save as CSV
weather_df = pd.DataFrame([weather_data])
covid_df = pd.DataFrame([covid_data])

weather_df.to_csv('data/weather_data.csv', index=False)
covid_df.to_csv('data/covid_data.csv', index=False)
