import streamlit as st
import pandas as pd
from PIL import Image
import xlrd
import streamlit.components.v1 as components
import lyricsgenius as genius
import time

# FOR DATA FETCHING
access_token = "eMiXYR0GF3D5dBmYyjqke6STCiR3MoWJ6sMZFwe4AG14vIwLvuZ8qRRzK157HKcd"


''' # Information Retrieval Project '''

song_list = pd.read_csv('Data.csv')

df = song_list.drop_duplicates(subset=['genre'], keep='first')

image = Image.open('Image.jpeg')
st.sidebar.image(image, caption='', use_column_width=True)
st.sidebar.header('Choose option to visualize')
st.sidebar.subheader('Select the following sentiment:')

input_artist = st.text_input('Search for song')

input_sentiment = st.selectbox('Select sentiment', options=[
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
st.button("submit")
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)


if(input_artist != ""):
    api = genius.Genius(access_token)
    variable = "hello"
    list_lyrics = []
    list_title = []
    list_artist = []
    list_album = []
    list_year = []

    for i in range(5):
        artist = api.search_artist(
            input_artist, max_songs=1, sort='popularity')
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {(i+1)*20}%')
        bar.progress((i+1)*20)
        time.sleep(0.1)
    for song in artist.songs:
        list_lyrics.append(song.lyrics)
        list_title.append(song.title)
        list_artist.append(song.artist)
    for i in range(5):
        components.html(
            """
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            <div id="accordion">
            <div class="card">
                <div class="card-header" id="headingOne">
                <h5 class="mb-0">
                    <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                    Collapsible Group Item #1
                    </button>
                </h5>
                </div>
                <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
                <div class="card-body">
                {list_title}
                </div>
                </div>
            </div>
            <div class="card">
                <div class="card-header" id="headingTwo">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                    Collapsible Group Item #2
                    </button>
                </h5>
                </div>
                <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                <div class="card-body">
                    Collapsible Group Item #2 content
                </div>
                </div>
            </div>
            </div>
            """.format(list_title=list_title[i]),
            height=150,
        )
