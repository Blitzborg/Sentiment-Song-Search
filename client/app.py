import streamlit as st
import pandas as pd
from PIL import Image
import xlrd

''' # Information Retrieval Project '''

song_list = pd.read_csv('Data.csv')

df = song_list.drop_duplicates(subset=['genre'], keep='first')

image = Image.open('Image.jpeg')
st.sidebar.image(image, caption='', use_column_width=True)
st.sidebar.header('Choose option to visualize')
st.sidebar.subheader('Select the following sentiment:')

text_input_box1 = st.text_input('Search for song')

text_input_box1 = st.selectbox('Select sentiment', options=[
                               'Positive', 'Neutral', 'Negative'])
#sentiment_box = st.select_slider('Select the following sentiment: ', options= ['Positive','Neutral', 'Negative'])
# """
# left, right, center = st.beta_columns(3)
# with left:
#     st.button('Positive')
# with right:
#     st.button('Neutral')
# with center:
#     st.button('Negative')
# """

principal_graphs_checkbox = st.sidebar.checkbox('Results', value=True)
principal_graphs_checkbox1 = st.sidebar.checkbox(
    'Dashboard Analytics', value=True)

text_input_box = st.text_area('Search for lyrics')

ticker = st.multiselect('Select the genre from the list below:', df['genre'])
hide_streamlit_style = """
            <style>
        
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
