import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the next days")

place = st.text_input("City: ")

days = st.slider("Forecast Days",
          min_value=1,
          max_value=5,
          help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} day(s) in {place}")

if place:
    filtered_data = get_data(place, days)
    print(filtered_data)
    if filtered_data is None:
        st.subheader("Cannot Fetch Data")

    elif filtered_data == 404:
        st.subheader("City Not Found")

    else:

        if option == "Temperature":
            temperatures = [dictionary["main"]["temp"] for dictionary in filtered_data]
            dates = [dictionary["dt_txt"] for dictionary in filtered_data]


            figure = px.line(x=dates,
                             y=temperatures,
                             labels={"x": "Dates", "y": "Temperatures (C)"})
            st.plotly_chart(figure)

        if option == "Sky":

            images = {"Clear": "assets/clear.png",
                      "Clouds": "assets/cloud.png",
                      "Rain": "assets/rain.png",
                      "Snow": "assets/snow.png"}

            sky_conditions = [dictionary["weather"][0]["main"] for dictionary in filtered_data]
            print(sky_conditions)

            image_paths = [images[condition] for condition in sky_conditions]
            print(image_paths)

            st.image(image_paths, width=115)