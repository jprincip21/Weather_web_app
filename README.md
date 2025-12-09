# 🌦️ Weather Forecast App

A simple Streamlit web application that displays the temperature or sky conditions for the next 1–5 days using the OpenWeatherMap API.

##🚀 Features

- Search weather forecast by city name

- View temperature trends as an interactive Plotly line chart

- Display sky conditions using icons (Clear, Clouds, Rain, Snow)

- Choose forecast duration (1–5 days)

- Clean and simple UI powered by Streamlit

- API key stored securely using .env

## 🔑 Setup
### Install dependencies
```
pip install -r requirements.txt
```

Create a .env file

- Create a file named .env in the project root:
```
API_KEY=your_openweathermap_api_key_here
```
You can get a free API key from:
https://openweathermap.org/api

## ▶️ Running the App

Start the Streamlit server:
```
streamlit run app.py
```
## 🧠 How It Works
### Frontend (main.py)

- Takes user input: city, number of days, and display option

- Calls get_data() from backend.py

- Displays:

  - Line chart of temperatures (Plotly)

  - Weather condition images (Streamlit + assets)

###  Backend (backend.py)

- Loads the API key from .env

- Sends request to OpenWeatherMap 5-day forecast endpoint

- Converts 3-hour interval data into day slices

- Returns parsed JSON

## 🖼️ Weather Icons

- Images are loaded from the assets/ folder based on API condition:

  - Clear → clear.png

  - Clouds → cloud.png

  - Rain → rain.png

  - Snow → snow.png

## ❗ Error Handling

- City not found → “City Not Found”

- Network or API error → “Cannot Fetch Data”

- No input → No request made