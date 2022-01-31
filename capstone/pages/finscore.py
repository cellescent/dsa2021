# This page shows visualizations related to the final score of each participant, with a set of filters that can be used to exclude or include only participants within certain demographics.
# Of particular note are the participants excluded by default. I selected two groups for this measure.
# The first are the participants below age 19. There exists only one participant in this category, whose age was entered as 0. This is obviously a typo, and thus the participant may be excluded on the grounds of avoiding having a misleading outlier.
# This second are the participants whose self-reported location didn't match any of the 50 states in the USA. Some of these are typos, while others are simply the only participant from their location. For simplicity's sake, the whole lot are excluded by default under the "Other" category.

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def app(data):
    st.title('Final Scores')
    
    st.markdown('### Filters')
    
    age_min = int(data.age.min())
    age_max = int(data.age.max())
    age_fmin, age_fmax = st.slider('Age Range', age_min, age_max, (11,age_max))
    
    rt_min = int(data.rt_total.min())
    rt_max = int(data.rt_total.max())
    rt_fmin, rt_fmax = st.slider('Total Response Time Range', rt_min, rt_max, (rt_min,rt_max))

    if st.checkbox('Exclude all locations'):
        fstate = st.multiselect('Exclude by location:', data.us.unique(),data.us.unique())
    else:
        fstate = st.multiselect('Exclude by location:', data.us.unique(), ['Other'])
    
    fgen = st.multiselect('Exclude by gender:', data.gender.unique())
    fhc = st.multiselect('Exclude by home computer access:', data.home_computer.unique())

    df = data.query('age>= @age_fmin and age <= @age_fmax and rt_total>= @rt_fmin and rt_total <= @rt_fmax and us not in @fstate and gender not in @fgen and home_computer not in @fhc')


    st.markdown('## Comparing Total Response Time to Final Score within Filtered Data')
    fig = px.scatter(
        df, x="rt_total", y="sum_score", log_x=True,
        labels={"sum_score":"Final Score", "rt_total":"Total Response Time (seconds)"}
    )
    st.plotly_chart(fig)

    st.markdown('## Comparing Final Score to Gender and Home Computer Access within Filtered Data')
    fig_hist = px.histogram(
        df, x='sum_score', 
        color="gender", 
        pattern_shape="home_computer",
        barmode="overlay",
        labels={"sum_score":"Final Score", "gender":"Gender", "home_computer":"Home Computer Access"}
    )
    st.plotly_chart(fig_hist)