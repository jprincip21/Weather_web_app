import requests
from dotenv import load_dotenv
import os

def get_data(place, forecast_days=None):

    days = forecast_days * 8 # Days are broken into increments of 3 hours. One day = 8 points

    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&cnt={days}&units=metric&appid={API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
        filtered_data = data["list"]
        return filtered_data

    if response.status_code == 404:
        return 404

    return None


if __name__  == "__main__":
    get_data(place="Tokyo", forecast_days=3)