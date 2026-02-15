import streamlit as st
from pyowm import OWM
import matplotlib.pyplot as plt

API_KEY = "1440671c483e78f4346df6569f3c634b"

# Create OWM object
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# ------------------ PLOTTING FUNCTIONS ------------------

# Bar Chart Function
def plot_bar_chart(days, temp_min, temp_max):
    plt.figure(figsize=(10,5))
    plt.bar(days, temp_min, label="Min Temperature")
    plt.bar(days, temp_max, bottom=temp_min, label="Max Temperature")
    plt.xlabel("Days")
    plt.ylabel("Temperature (°C)")
    plt.title("5 Day Weather Forecast - Bar Chart")
    plt.legend()
    st.pyplot(plt)

# Line Chart Function
def plot_line_chart(days, temp_min, temp_max):
    plt.figure(figsize=(10,5))
    plt.plot(days, temp_min, marker='o', label="Min Temperature")
    plt.plot(days, temp_max, marker='o', label="Max Temperature")
    plt.xlabel("Days")
    plt.ylabel("Temperature (°C)")
    plt.title("5 Day Weather Forecast - Line Chart")
    plt.legend()
    st.pyplot(plt)

# ------------------ STREAMLIT UI ------------------

st.title("Weather Forecast App")

city = st.text_input("Enter City Name")

unit = st.selectbox("Select Temperature Unit", ["Celsius", "Fahrenheit"])

graph_type = st.selectbox("Select Graph Type", ["Bar Chart", "Line Chart"])

# ------------------ FETCH WEATHER ------------------
if city:
    forecaster = mgr.forecast_at_place(city + ", IN", "3h")
    forecast = forecaster.forecast
    weather_list = forecast.weathers

    daily_data = {}

    # Collect all temperatures day-wise
    for w in weather_list:
        date = w.reference_time("iso")

        temp = w.temperature("celsius")
        t_min = temp["temp_min"]
        t_max = temp["temp_max"]

        if date not in daily_data:
            daily_data[date] = {
                "min_temps": [],
                "max_temps": []
            }

        daily_data[date]["min_temps"].append(t_min)
        daily_data[date]["max_temps"].append(t_max)

    # Now calculate real daily min & max
    days = []
    temp_min = []
    temp_max = []

    for date in daily_data:
        days.append(date)
        temp_min.append(min(daily_data[date]["min_temps"]))
        temp_max.append(max(daily_data[date]["max_temps"]))

    # Plot graph
    if graph_type == "Bar Chart":
        plot_bar_chart(days, temp_min, temp_max)
    else:
        plot_line_chart(days, temp_min, temp_max)