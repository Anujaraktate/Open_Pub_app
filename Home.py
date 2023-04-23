import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(layout="wide")
st.title("🍻Pubs In United Kingdom To Have Some Drink And Chillout🍻")
st.write('By: :black[Anuja Raktate]')


st.subheader(":green[Connect with me on,]")

col1,col2,col3,col4=st.columns(4, gap='small')
with col1:
    st.subheader("[LinkedIn](https://www.linkedin.com/in/anujaraktate/)")
with col2:
    st.subheader("[GitHub](https://github.com/Anujaraktate)")

#Background Image
page_bg_img = '''
<style>
.stApp {
background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.erieinsurance.com%2Fblog%2Fnew-years-eve-safety-tips&psig=AOvVaw1nSIcbpY029belCQTYjTVg&ust=1682271284026000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCOjhr4qDvv4CFQAAAAAdAAAAABAk");
background-size: cover;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

#Page Heading
st.header("🍺🍸All Pubs Information in United Kingdom🍺🍸")

#Background Image
page_bg_img = '''
<style>
.stApp {
background-image: url("https://media.bizj.us/view/img/10779959/gettyimages-841024284*1024xx5400-3038-0-211.jpg");
background-size: cover;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

#Reading data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resourses")
DATA_PATH1 = os.path.join(dir_of_interest, "open_pubs_clean.csv")
df = pd.read_csv(DATA_PATH1)
with st.expander(label='Click Here to see the dataset overview',expanded=False):
    st.dataframe(df)

#Unique Bars and Local Authorities
unique=['Number of Pubs', 'Number of Local Authorities','Number of Postal Code']

option=st.radio(label="Select below options to see total count",
                options=unique,label_visibility="visible", horizontal=True)

if option=='Number of Pubs':
    st.subheader(f"Total Pubs in UK: :blue[{df['name'].nunique()}]")
elif option=='Number of Postal Code':
    st.subheader(f"Total Post Codes in UK: :blue[{df['postcode'].nunique()}]")
else:
    st.subheader(f"Total Local Authorities in UK :blue[{df['local_authority'].nunique()}]")

st.subheader(":red[🥂🍹Pubs are at the heart of British communities and serve as places for friends to gather, people to relax and unwind and stories to be told🥂🍹.]")