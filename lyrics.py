import pandas as pd
#from google.colab import drive
#import warnings
#warnings.simplefilter(action='ignore', category=FutureWarning)
import lyricsgenius
from datetime import datetime
import sys
import re

client_id = 'TS15U5iwbWLGkhfGFVqnOuDA9mVjJhhLlXpJDYai6nm79S9JWFzznlsQN5dCFuZG'
client_secret = 'SOhrXQxD9YZ2RxBQwR-wwu5Zbxh6UgkfuIEaUJltx9L9h8aynN5zZ9Jsm1JNlh_5Npu_uev1MKorJV_A6MVYKw'
access_token = 'US00oQ6_8lkhwRjHAOudB62bruf1B3JGOGuHR8V8zeawxpoc8fcA9QGXQ3bhYWu-'
website_url = 'https://github.com/Joseph-Willem-Ricci/5450-final-project'

api = lyricsgenius.Genius(access_token, retries = 500, remove_section_headers = True)
#artist = genius.search_artist('Andy Shauf')
#artist.save_lyrics()

df_combined_features = pd.read_csv('combined_features.csv')

all_song_data = pd.DataFrame()
start_time = datetime.now()
print("Started at {}".format(start_time))
for i in range((1924+3678), len(df_combined_features)):
    rolling_pct = int((i/len(df_combined_features))*100)
    print(str(rolling_pct) + "% complete." + " Collecting Record " + str(i) +" of " +
          str(len(df_combined_features))+ "." + " Currently collecting " + 
          df_combined_features.iloc[i]['title'] + " by " + df_combined_features.iloc[i]['artist'] + " "*50, end="\r")
    song_title = df_combined_features.iloc[i]['title']
    song_title = re.sub(" and ", " & ", song_title)
    artist_name = df_combined_features.iloc[i]['artist']
    artist_name = re.sub(" and ", " & ", artist_name)

    try:
        song = api.search_song(song_title, artist=artist_name)
        #print(song)
        #song_album = song.album
        #song_album_url = song.album_url
        #featured_artists = song.featured_artists
        song_lyrics = re.sub("\n", " ", song.lyrics) #Remove newline breaks, we won't need them.
        #song_media = song.media
        song_url = song.url
        #song_writer_artists = song.writer_artists
        #song_year = song.year
    except:
        #song_album = "null"
        #song_album_url = "null"
        #featured_artists = "null"
        song_lyrics = "null"
        #song_media = "null"
        song_url = "null"
        #song_writer_artists = "null"
        #song_year = "null"
        
    row = {
        #"Year": df_combined_features.iloc[i]['Year'],
        #"Rank": df_combined_features.iloc[i]['Rank'],
        "title": df_combined_features.iloc[i]['title'],
        "artist": df_combined_features.iloc[i]['artist'],
        #"Album": song_album,
        #"Album URL": song_album_url,
        #"Featured Artists": featured_artists,
        "lyrics": song_lyrics,
        #"Media": song_media,
        "song URL": song_url,
        #"Writers": song_writer_artists,
        #"Release Date": song_year
    }
    all_song_data = all_song_data.append(row, ignore_index=True)
    all_song_data.to_csv("all_song_data_final_3.csv")
end_time = datetime.now()
print("\nCompleted at {}".format(start_time))
print("Total time to collect: {}".format(end_time - start_time))




