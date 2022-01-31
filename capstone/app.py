from pages import landing, sample, finscore, itemscore, final
import streamlit as st
import pandas as pd
import numpy as np
import re

PAGES = {
    "About": landing,
    "Demographics": sample,
    "Final Score Visualization": finscore,
    "Item Score Visualizations": itemscore,
    "Notes": final
}

selection = st.sidebar.radio("Navigation", list(PAGES.keys()))


DATA_URL = ('https://raw.githubusercontent.com/cellescent/dsa2021/main/capstone/data_capstone_dsa2021_2022.csv')
STATES_URL = ('https://raw.githubusercontent.com/cellescent/dsa2021/main/capstone/pages/states.csv')


sdf = pd.read_csv(STATES_URL)
sdf = sdf.reset_index()

def strans(s):
    sl = re.findall(r"[\w']+|[.,!?;]", s.upper())
    for l in sdf.State.unique():
        if(l.upper() in s.upper()): # state name is explicitly in text
            return l
        else:
            if(any([sdf.loc[sdf.State==l].Abbreviation.iloc[0] == w for w in sl])): # state abbreviation found by itself
                return l
    return "Other"
    

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    data['us'] = data.state.apply(strans)
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Data loaded! (using st.cache)")

#if st.checkbox('Show raw data'):
#    st.subheader('Raw data')
#    st.write(data)

page = PAGES[selection]
page.app(data)