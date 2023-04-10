import pandas as pd

df_lyrics_1 = pd.read_csv('all_song_data_final.csv', low_memory=False)
df_lyrics_2 = pd.read_csv('all_song_data_final_2.csv', low_memory=False)
df_lyrics_3 = pd.read_csv('all_song_data_final_3.csv', low_memory=False)

lyrics_list = [df_lyrics_1, df_lyrics_2, df_lyrics_3]

df_lyrics = pd.concat(lyrics_list)

df_lyrics.drop_duplicates(inplace = True)

#print(df_lyrics[df_lyrics['song URL'].isna()])

#print(df_lyrics[df_lyrics.apply(lambda r: r.str.contains('annotated', case=False).any(), axis=1)])

print(df_lyrics.shape)

df_lyrics = df_lyrics[df_lyrics.apply(lambda r: ~r.str.contains('annotated', case=False).any(), axis=1)]

#df_lyrics = df_lyrics[~df_lyrics['song URL'].str.contains('annotated')]

print(df_lyrics.shape)

df_lyrics.dropna(subset = ['title', 'artist', 'lyrics'],inplace = True)

print(df_lyrics.shape)

#df_lyrics = df_lyrics[df_lyrics.apply(lambda r: ~r.columns.str.contains("Unnamed", case=False).any(), axis=1)]

df_lyrics = df_lyrics[['title', 'artist', 'lyrics', 'song URL']]

print(df_lyrics.head(10))

#df_lyrics = df_lyrics.loc[:, ~df_lyrics.columns.str.contains("Unnamed")]

#df_lyrics.to_csv("all_song_data_complete.csv")

#df_lyrics_two = df_lyrics.apply(lambda x: ~x['song URL'].contains(x['title']), axis=1)

df_lyrics.dropna(inplace = True)

#df_lyrics = df_lyrics[~df_lyrics['song URL'].str.contains('chapter')]

#df_lyrics_two = df_lyrics[~df_lyrics['song URL'].str.contains('discography')]

#df_lyrics_two = df_lyrics[df_lyrics.apply(lambda x: x['artist'].replace(" ", "-").lower() not in x['song URL'].lower(), axis=1)]

df_lyrics['clean URL'] = df_lyrics['song URL'].str.replace('-', '').str.lower()
df_lyrics['clean artist'] = df_lyrics['artist'].str.replace(' ', '').str.lower()

df_lyrics['URL letters'] = df_lyrics['clean URL'].str.extract(r'https://genius\.com/(\w{2})')

#print(df_lyrics.head(10))

df_lyrics_two = df_lyrics.loc[df_lyrics['URL letters'] == df_lyrics['clean artist'].str[:2]]

df_lyrics_three = df_lyrics.loc[df_lyrics['URL letters'] != df_lyrics['clean artist'].str[:2]]

#print(df_lyrics_two)

print(df_lyrics_two.head(10))

print(df_lyrics_three.head(10))

#print(df_lyrics.loc[df_lyrics['title'] == 'Siren Song'])

#print(df_lyrics_two.loc[df_lyrics_two['title'] == 'Empty Space - Vevo Live Acoustic'])

print(df_lyrics_two.loc[df_lyrics_two['title'] == 'Siren Song'])
#print(df_lyrics_three.loc[df_lyrics['title'] == 'Siren Song'])


#print(df_lyrics[~df_lyrics['song URL'].str.contains(df_lyrics['title'])])

#.str.replace(' ', '', regex=True)