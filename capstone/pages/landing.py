# This is the first page that appears on the site. Rather than immediately overwhelming the viewer with figures, it provides a very simple explanation of the content of the site.

import streamlit as st

def app(data):
    st.title('About')
    
    st.write("This page was created by **Jason Xie** of the **Process Data Group** as a final project for the ETS Data Science Academy 2022 led by Oren Livne, Jiangang Hao, and Qiwei He. The intent of this project is to develop a dashboard based on a set of data provided by the course's instructors. The source code for this project, and the raw data described within, can be found at [my GitHub repository for the DSA](https://github.com/cellescent/dsa2021/tree/main/capstone). A copy of the raw data can also be viewed below.")
    
    if st.checkbox('Display raw data'):
        st.subheader('Raw data')
        st.write(data.loc[:, data.columns != 'us'])
    
    st.write("Use the radio buttons on the sidebar at the left to navigate between pages. For any further questions or concerns, contact jxie@ets.org")