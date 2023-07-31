import streamlit as st
from backend import get_data
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select day(s) to see the weather forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures,
                         labels={"x": "Date", "y": "Temperatur (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in filtered_data]
        st.image(image_paths, width=115)