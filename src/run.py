import json

import numpy as np
import seaborn as sns
import streamlit as st 
import matplotlib.pyplot as plt 
from PIL import Image


#Log in and Sign up
Login_option = st.sidebar.radio('Login/Signup', ('Login', 'Signup'))

if Login_option =='Login':

    with st.sidebar.form("Login"):
        st.write("Login Here")
        username = st.text_input ("Username")
        password = st.text_input("Password", type="password")

        #Every form must have a submit button.
        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("signup"):
        st.write("Signup Here")
        username = st.text_input ("Username")
        password = st.text_input("Password", type="password")
        emial = st.text_input("Email")


        #Every form must have a submit button.
        submitted = st.form_submit_button("Signup")
        if submitted:
            pass

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

st.title(':zap: Pytopia Dashnoard')

#Banner
banner = Image.open('./data/banner.png')
st.image(banner)

#Metrics
col1, col2 = st.columns(2)
col1.metric(label="Telegram Members", value="4800", delta="100")
col2.metric(label="Pythopia Website Members", value="2102", delta="8")

#Statestics
with st.expander("Statistics"):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)

#User Info
with st.expander('User Profile:'):
    col1, col2 = st.columns(2)
    col1.text_input('Name:')
    col2.text_input('Location:')
    st.camera_input('Camera Input', key='camera_input')



