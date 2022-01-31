import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def app(data):
    st.title('Individual Item Scores')

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
    
    st.markdown('### Examine Individual Item')
    fitem = st.slider('', 1, 20)
    
    gs = "gs_" + str(fitem)
    rt = "rt_gs_" + str(fitem)
    
    if(fitem==1):
        st.write("There is no data regarding response time to the first item. Select an item between 2 and 20 to display #data comparing response time to score on individual items.")
    else:
        st.markdown('## Comparing Item Response Time to Final Score within Filtered Data')
        dfc = df.copy()
        dfc[gs] = df[gs].astype(str)
        
        #data_canada = px.data.gapminder().query("country == 'Canada'")
        fig = px.scatter(
            dfc, x=rt, y="sum_score", color=gs, log_x=True,
            labels={gs:"Score on item {}".format(fitem), rt:"Response Time to item {} (seconds)".format(fitem),
                        "sum_score":"Final Score"
                    }
        )
        st.plotly_chart(fig)
    
    st.markdown('## Comparing Item Score to Gender and Home Computer Access within Filtered Data')
    fig_hist = px.histogram(
        df, x=gs, 
        color="gender", 
        pattern_shape="home_computer",
        barmode="group",
        labels={gs:"Score on item {}".format(fitem), "gender":"Gender", "home_computer":"Home Computer Access"}
    )
    st.plotly_chart(fig_hist)
    
    