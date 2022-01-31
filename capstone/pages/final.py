import streamlit as st

def app(data):
    st.title('Notes')
    st.write("As can be seen on the demographics page, a significant number of participants reported taking the test from nonstandard locations designated within as \"Other\", which may have either been outside of the 50 states in the U.S., or typos. There is also a participant whose age was listed as 0. These participants may be designated as outliers and removed from analysis. As such, the visualization pages default to excluding their data. The Age filter is set to default to a minimum age of 11, the youngest valid age in the dataset; the Location filter is set to default to excluding data tagged with the Other location, that is to say data outside of the 50 United States.")