import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components
import requests
from typing_extensions import final
import json
import emoji
import base64
import time

st.title(emoji.emojize(':musical_note: SongGenius :musical_note:'))
img = Image.open('landing_image.jpg')
st.image(img, caption='', use_column_width=True)

image = Image.open('LyricsGenius.png')
st.sidebar.header("Song data provided by: ")
st.sidebar.image(image, caption='', use_column_width=True)
st.sidebar.header('Search for songs by: ')

song_input = " "
sentiment_input = " "
artist_input = " "
lyrics_input = " "
genre_input = " "

# search_by = st.sidebar.radio(
#    "", ('Song Name', 'Sentiment', 'Lyrics', 'Artist', 'Genre'))

check_sn = st.sidebar.checkbox('Song Name')
check_sentiment = st.sidebar.checkbox('Sentiment')
check_artist = st.sidebar.checkbox('Artist')
check_lyrics = st.sidebar.checkbox('Lyrics')
check_genre = st.sidebar.checkbox('Genre')

num_results = st.sidebar.slider(
    "How many results would you like to see?", min_value=1, max_value=50, value=10)

st.sidebar.header(emoji.emojize('For nerds :nerd_face:'))

if check_sn is True:
    '''## Select by Song'''
    song_input = st.text_input('E.g. Shape of you')
if check_sentiment is True:
    '''## Select by Sentiment'''
    sentiment_input = st.selectbox('What kind of songs would you like to hear?', options=[
                                   "Happy", "Sad", "Anything is fine!"])
if check_lyrics is True:
    '''## Select by Lyrics'''
    lyrics_input = st.text_area('E.g. I\'m in love with the shape of you ')
if check_artist is True:
    '''## Select by Artist'''
    artist_input = st.text_input('E.g. Ed Sheeran')
if check_genre is True:
    '''## Select by Genre'''
    genre_input = st.selectbox('Tip: Select one of the dropdown below', options=['', 'Acoustic Blues', 'Alternative', 'Alternative Country', 'Americana', 'Bluegrass', 'Blues-Rock', 'British Invasion', 'College Rock', 'Comedy', 'Contemporary Country', 'Contemporary R&B', 'Country', 'Electronic', 'Grunge', 'Hardcore', 'Hip-Hop', 'Hip-Hop/Rap', 'House', 'Indian Pop',
                                                                                     'Inspirational', 'Jazz', 'Latin', 'Metal', 'Misc', 'Outlaw Country', "Pop", 'Pop/Rock', 'Prog-Rock/Art Rock', 'Punk', 'R&B', 'R&B/Soul', 'Rap', 'Reggae', 'Reggaeton y Hip-Hop', 'Rock', 'Rock & Roll', 'Salsa & Tropical', 'Singer/Songwriter', 'Soul', 'Southern Rock', 'Teen Pop', 'Traditional Country', 'Vocal Jazz', 'World/International', 'World/Reggae'])

submit = st.button("Search")
# results = st.sidebar.slider(
#    "Show top results", min_value=1, max_value=50, step=1)
principal_graphs_checkbox1 = st.sidebar.checkbox('Dashboard Analytics')

genre_dict = {
    "Inspirational": "Inspirational",
    "Jazz": "Jazz",

    "Latin": "Latin",
    "Metal": "Metal",
    "Misc": "Misc",
    "Outlaw Country": "Outlaw%20Country",
    "Pop/Rock": "Pop%2FRock",
    "Prog-Rock/Art Rock": "Prog-Rock%2FArt%20Rock",
    "R&B": "R%26B",
    "R&B/Soul": "R%26B%2FSoul",
    "Reggaeton y Hip-Hop": "Reggaeton%20y%20Hip-Hop",
    "Rock & Roll": "Rock%20%26%20Roll",
    "Salsa & Tropical": "Salsa%20%26%20Tropical",
    'Acoustic Blues': 'Acoustic%20Blues', 'Alternative': 'Alternative', 'Alternative Country': 'Alternative%20Country', 'Americana': 'Americana', 'Bluegrass': 'Bluegrass', 'Blues-Rock': 'Blues-Rock', 'British Invasion': 'British%20Invasion', 'College Rock': 'College%20Rock', 'Comedy': 'Comedy', 'Contemporary Country': 'Contemporary%20Country', 'Contemporary R&B': 'Contemporary%20R%26B', 'Country': 'Country', 'Electronic': 'Electronic', 'Grunge': 'Grunge', 'Hardcore': 'Hardcore', 'Hip-Hop': 'Hip-Hop', 'Hip-Hop/Rap': 'Hip-Hop%2FRap', 'House': 'House', 'Indian Pop': 'Indian%20Pop', 'Singer/Songwriter': 'Singer%2FSongwriter', 'Soul': 'Soul', 'Southern Rock': 'Southern%20Rock', 'Teen Pop': 'Teen%20Pop', 'Traditional Country': 'Traditional%20Country', 'Vocal Jazz': 'Vocal%20Jazz', 'World/International': 'World%2FInternational', 'World/Reggae': 'World%2FReggae'

}


def query_list_prep(list_of_strings):
    k = 0
    if(len(list_of_strings) == 1):
        return list_of_strings
    #final_list = []
    for k in range(len(list_of_strings)):
        if(k == len(list_of_strings) - 1):
            continue
        else:
            list_of_strings[k] = list_of_strings[k] + "%20"
    return list_of_strings


def listToString(list_of_strings):
    final_string = ""
    if(list_of_strings == []):
        final_string = ""
    else:
        for string in list_of_strings:
            final_string += string
    return final_string


start_time = 0
end_time = 0


def generateCards(search_by, jsonObject, type, submit=submit):
    # if len(search_by) > 0 and submit == True:
    if search_by > 0 and submit == True:
        result_size = len(jsonObject)
        st.write("{} result(s) found".format(result_size))

        for i in range(result_size):
            lyric_text = "No lyrics found"
            exp_rating = "No rating found"
            about_artist = "No artist data available"
            color = ""
            yt_link = jsonObject[i]["link"]
            sentiment_final = jsonObject[i]["sentiment"]
            if("lyrics" in jsonObject[i]):
                lyric_text = jsonObject[i]["lyrics"].replace("\n", "<br />")
                exp_rating = jsonObject[i]["explicit_rating"]
            if("artist_details" in jsonObject[i]):
                about_artist = jsonObject[i]["artist_details"][0].replace(
                    "\n", "<br />")
            if(sentiment_final == "positive"):
                color = "green"
            elif(sentiment_final == "neutral"):
                color = "#E9DF18"
            else:
                color = "red"
            final_link = yt_link.replace("watch?v=", "embed/")
            components.html(
                """
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div id="accordion" style="max-height: 100; overflow-y:auto;">
                <div class="card" >
                    <div class="card-header" id="headingOne">
                    <h5 class="mb-0">
                        <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                        {artist_name} : {artist_song}
                        </button>
                    </h5>
                    
                    </div>
                    <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
                    <div class="card-body" >
                        <div style="float:left">
                        <iframe width="300" height="200" src={yt_link} >
                        </iframe>
                        </div>
                        
                        <div style="float:center">
                        <div width="200">
                        <h5 style="color:{color}">Sentiment: {sentiment}</h5>
                        <h5>Explicit rating: {exp_rating}</h5>
                        <h5>Genre: {genre}</h5>

                       

                        <button type="button" class="btn btn-warning" data-toggle="modal" data-target="#lyricsModal">
                            Song Lyrics
                        </button>
                        <button type="button" class="btn btn-warning" data-toggle="modal" data-target="#artistModal">
                            About the artist
                        </button>
                        <br />
                        <br />
                        <button type="button" class="btn btn-danger" onclick=" window.open('{original_link}', '_blank'); return false;">
                            Watch on YouTube
                        </button>


                        <div class="modal fade" id="lyricsModal" tabindex="-1" role="dialog" aria-labelledby="lyricsModalLabel" aria-hidden="true">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="lyricsModalLabel">Song lyrics</h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div class="modal-body">
                                {lyrics}
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                            </div>
                            </div>
                        </div>
                        </div>

                        <div
                        class="modal fade"
                        id="artistModal"
                        tabindex="-1"
                        role="dialog"
                        aria-labelledby="artistModalLabel"
                        aria-hidden="true"
                        >
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="artistModalLabel">About {artist_name}</h5>
                                <button
                                type="button"
                                class="close"
                                data-dismiss="modal"
                                aria-label="Close"
                                >
                                <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div class="modal-body">{artist_deets}</div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                
                            </div>
                            </div>
                        </div>
                        </div>


                        
                        </div>
                       
                    </div>
                        
                    </div>
                    </div>
                </div>
                </div>
                """.format(artist_name=str(jsonObject[i]["_artist"][0]), artist_song=str(jsonObject[i]["song_name"][0]), yt_link=final_link, artist_deets=about_artist, exp_rating=exp_rating, sentiment=sentiment_final, genre=jsonObject[i]["genre"], lyrics=lyric_text, original_link=jsonObject[i]["link"], color=color),
                height=302,
            )
    end_time = time.time()
    print(end_time - start_time)


dict_searchCriteria = {
    "name": [check_sn, "song_name", song_input],
    "artist": [check_artist, "_artist", artist_input],
    "lyrics": [check_lyrics, "lyrics", lyrics_input],
    "sentiment": [check_sentiment, "sentiment", sentiment_input],
    "genre": [check_genre, "genre", genre_input]
}

dict_sentiments = {
    "Happy": "positive",
    "Anything is fine!": "neutral",
    "Sad": "negative"
}
###### backend api interaction ########
if(submit is True):
    url = "http://localhost:8983/solr/songs/select?q="
    i = 0
    for key, value in dict_searchCriteria.items():
        if(value[0] is True):
            if(key != "genre" and key != "sentiment"):
                i += 1
                if(i > 1):
                    url += "%20AND%20"
                url += value[1] + "%3A%22"
                split = value[2].split(" ")
                list_query = query_list_prep(split)
                string_query = listToString(list_query)
                url += string_query + "%22"
            elif(key == "sentiment"):
                i += 1
                if(i > 1):
                    url += "%20AND%20"
                selection = dict_sentiments[sentiment_input]
                url += value[1] + "%3A%22" + selection + "%22"

            elif(key == "genre"):
                i += 1
                if(i > 1):
                    url += "%20AND%20"
                url += value[1] + "%3A%22"
                genre_query = ""
                if(value[2] not in genre_dict.keys()):
                    genre_as_list = value[2].split(" ")
                    genre_string = query_list_prep(genre_as_list)
                    genre_query = listToString(genre_string)
                else:
                    genre_query = genre_dict[genre_input]
                url += genre_query + "%22"
    url += "&rows={}".format(num_results)
    start_time = time.time()
    response = requests.get(url)

    json_response = json.loads(response.text)
    # fix the search_by parameter in generateCards
    generateCards(1, json_response["response"]["docs"], submit)
    i = 0
    ###### hiding useless footer #############
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
