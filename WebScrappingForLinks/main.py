import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# <<<------   FOR THE LINK OF THE SONG    -------->>>>>>>>

data = pd.read_csv("songs_and_artists.csv")

data = data[data['track_name'].map(lambda x: x.isascii())]

# < < < < < ------     FOR SONG COLLECTION     ------ > > > > >

# print(data.iloc[])
#
# new_df = data[['track_name','artist_name']]
#
# # print(new_df.iloc[:100])
#
# new_df["songs_artists"] = new_df['track_name'] +" "+ new_df["artist_name"]
# new_df = new_df['songs_artists']
#
#
# col_list = new_df.values.tolist()
# list_a = col_list[5000:]
# # print(list_a)
#
# # Set up the Spotify API client
# client_id = '9ea8790afb7144bf821b4fa15b7a9324'
# client_secret = 'eed7059644854f428fe2898abc6957e3'
# client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#
# # # The list of songs to search for
# # song_list = ["mohabbat bhi jhoothi mukesh",
# # "i believe frankielaine",
# # ]
#
#
#
# # Create a CSV file and write header
# with open('spotify_links.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Song Name", "Spotify Link"])
#
#     # Loop through the list of songs
#     for song in list_a:
#         # Search for the song on Spotify
#         result = sp.search(q=song, type='track', limit=1)
#
#         # Check if any tracks were found
#         if result['tracks']['items']:
#             # Get the link to the first track in the results
#             track = result['tracks']['items'][0]
#             link = track['external_urls']['spotify']
#
#             # Write the song name and Spotify link to the CSV file
#             writer.writerow([song, link])
#         else:
#             # Write a message to the CSV file indicating that no results were found
#             writer.writerow([song, "No results found"])
#
# print("Done!")



# < < < < < ------     FOR IMAGE COLLECTION     ------ > > > > >

# Set up the Spotify API client
# data = pd.read_csv("songs_and_artists.csv")
#
# data = data[data['track_name'].map(lambda x: x.isascii())]
# print(data.iloc[5:15])

# new_df = data[['track_name','artist_name']]
# new_df["songs_artists"] = new_df['track_name'] +" "+ new_df["artist_name"]
# new_df = new_df['songs_artists']
#
# col_list = new_df.values.tolist()
# list_a = col_list[5000:]
#
# client_id = '9ea8790afb7144bf821b4fa15b7a9324'
# client_secret = 'eed7059644854f428fe2898abc6957e3'
# client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#
# # The list of songs to search for
# song_list = ["mohabbat bhi jhoothi mukesh","i believe frankielaine"]
#
# # Create a CSV file and write header
# with open('spotify_links.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Song Name", "Album Art Link"])
#
#     # Loop through the list of songs
#     for song in list_a:
#         # Search for the song on Spotify
#         result = sp.search(q=song, type='track', limit=1)
#
#         # Check if any tracks were found
#         if result['tracks']['items']:
#             # Get the link to the first track in the results
#             track = result['tracks']['items'][0]
#             # link = track['external_urls']['spotify']
#
#             # Get the link to the album art for the track
#             album_art_link = track['album']['images'][0]['url']
#
#             # Write the song name, Spotify link, and album art link to the CSV file
#             writer.writerow([song, album_art_link])
#         else:
#             # Write a message to the CSV file indicating that no results were found
#             writer.writerow([song, "No album art found"])
#
# print("Done!")
