
'''
import streamlit as st
from pyowm import OWM
from pyowm.utils.config import get_default_config

API_KEY = "1440671c483e78f4346df6569f3c634b"

# Configure PyOWM connection (avoid SSL verification issue)
config_dict = get_default_config()
config_dict["connection"]["use_ssl"] = True
config_dict["connection"]["verify_ssl_certs"] = False
config_dict["connection"]["timeout_secs"] = 10

owm = OWM(API_KEY, config_dict)
mgr = owm.weather_manager()

st.title("5 Day Weather Forecast")
st.write("### Write the name of a City and select the Temperature Unit and Graph Type from the sidebar")

place = st.text_input("NAME OF THE CITY :", "")
if not place:
    st.write("Input a CITY!")

unit = st.selectbox("Select Temperature Unit", ("Celsius", "Fahrenheit"))
g_type = st.selectbox("Select Graph Type", ("Line Graph", "Bar Graph"))

if place:
    try:
        # Forecaster object (high-level interface)
        forecaster = mgr.forecast_at_place(place + ", IN", interval="3h")

        # Forecast object (actual list of Weather objects)
        forecast = forecaster.forecast

        temps = []
        times = []
        for w in forecast:
            times.append(w.reference_time("iso"))
            if unit == "Celsius":
                temps.append(w.temperature("celsius")["temp"])
            else:
                temps.append(w.temperature("fahrenheit")["temp"])

        st.write(f"### 5 Day / 3‑hour forecast for {place}")

        # Show as line or bar chart
        import pandas as pd
        df = pd.DataFrame({"time": times, "temp": temps}).set_index("time")

        if g_type == "Line Graph":
            st.line_chart(df)
        else:
            st.bar_chart(df)

    except Exception as e:
        st.error(f"Error fetching forecast: {e}")
'''