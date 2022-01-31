import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

STATES_URL = ('pages/states.csv')
sdf = pd.read_csv(STATES_URL)

def app(data):
    st.title('Demographics')
    
    demos = data.copy()[['gender', 'age', 'us', 'home_computer', 'state']].rename(
        columns = {'gender':'Gender', 'age':'Age', 'us':'Location', 'home_computer':'Home Computer Access'}
    )
    
    if st.checkbox('Show Demographic Data'):
        st.dataframe(demos[['Gender', 'Age', 'Location', 'Home Computer Access']])
    
    st.metric("Sample Size", len(demos))

    st.header("Gender")
    st.plotly_chart(go.Figure(
        go.Pie(
        labels = demos.Gender.value_counts().index,
        values = demos.Gender.value_counts().values,
        hoverinfo = "label+percent",
        textinfo = "value"
    )))
    
    st.header("Home Computer Access")
    st.plotly_chart(go.Figure(
        go.Pie(
        labels = demos['Home Computer Access'].value_counts().index,
        values = demos['Home Computer Access'].value_counts().values,
        hoverinfo = "label+percent",
        textinfo = "value"
    )))
    
    ldf = pd.DataFrame(demos.loc[demos.Location.isin(sdf.State.unique())].Location.value_counts())
    ldf.reset_index(inplace=True)
    ldf = ldf.rename(columns = {'index':'State', 'Location':'Count'})
    mdf = ldf.merge(sdf, on="State")
    mdf['text'] = mdf.apply(lambda x: "Number of Test-Takers in " + x.State + ': ' + str(x.Count), axis=1)

    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = mdf['Longitude'],
        lat = mdf['Latitude'],
        text = mdf['text'],
        marker = dict(
            size = mdf['Count'],#/scale,
            #color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        )
    ))
    fig.update_layout(
            title_text = 'Locations of test-takers within the United States',#<br>(Click legend to toggle traces)',
            showlegend = False,
            geo = dict(
                scope = 'usa',
                landcolor = 'rgb(217, 217, 217)',
            )
        )
    st.plotly_chart(fig)
    
    
    st.subheader('Other Locations')
    st.dataframe(demos.loc[demos.Location=="Other"].state.unique())