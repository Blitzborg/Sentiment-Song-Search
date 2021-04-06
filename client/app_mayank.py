import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components

''' # Information Retrieval Project '''

song_list = pd.read_excel('Song_data_prep (1).xlsx')

df = song_list.drop_duplicates(subset=['genre'],keep='first')

image = Image.open('Image.jpeg')
st.sidebar.image(image, caption='',use_column_width=True)
st.sidebar.header('Choose option to visualize')
st.sidebar.subheader('Select the following sentiment:')

text_input_box1 = st.text_input('Search for song')

text_input_box1 = st.selectbox('Search for song',options=['Positive','Neutral', 'Negative'])
#sentiment_box = st.select_slider('Select the following sentiment: ', options= ['Positive','Neutral', 'Negative'])

left, right,center = st.beta_columns(3)
with left:
    st.button('Positive')
with right:
    st.button('Neutral')
with center:
    st.button('Negative')


principal_graphs_checkbox = st.sidebar.checkbox('Results', value = True)
principal_graphs_checkbox1 = st.sidebar.checkbox('Dashboard Analytics', value = False)

text_input_box = st.text_area('Search for lyrics')

ticker = st.multiselect('Select the genre from the list below:',df['genre'])


x1 = st.button('Submit')


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
                Heading : {heading}
                </button>
            </h5>
            </div>
            <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
            <div class="card-body">
            {variable}
            </div>
            </div>
        </div>
        </div>
        """.format(variable=i,heading=i),
        height=150,
    )
