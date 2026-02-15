import pyowm
import streamlit as st

owm=pyowm.OWM('1440671c483e78f4346df6569f3c634badd')
mgr=owm.weather_manager() 

st.title("5 Day Weather Forecast")
st.write("### Write the name of a City and select the Temperature Unit and Graph Type from the sidebar")


place=st.text_input("NAME OF THE CITY :", "")
if place == None:
    st.write("Input a CITY!")

unit=st.selectbox("Select Temperature Unit",("Celsius","Fahrenheit"))

g_type=st.selectbox("Select Graph Type",("Line Graph","Bar Graph"))
