import streamlit as st
import pickle
import webbrowser
import numpy as np


from random import sample
from streamlit_player import st_player
from urllib3.connectionpool import xrange

st.set_page_config(layout="wide")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# // new_df = music_list_df
music_list_df = pickle.load(open('music.pkl', 'rb'))
# music_list = music_list_df['track_name'].values + music_list_df['image_link'].values + music_list_df['spotify_link'].values
music_list = music_list_df['track_name'].values
# print(music_list)
# // similarity
similarity = pickle.load(open('similarity.pkl', 'rb'))


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1524678606370-a47ad25cb82a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80");
             background-attachment: fixed;
             background-size: cover;
             filter: blur(8px);
            -webkit-filter: blur(8px);
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


# add_bg_from_url()

def recommend(music):
    # find index of the given song
    music_index = music_list_df[music_list_df['track_name'] == music].index[0]

    # set a variable that coincdes with that index in similarity array
    distances = similarity[music_index]

    # sort the distances but use enumerate to preserve the actual index of the song
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_music = []
    # make list of the top 5 movies
    for i in music_list:
        temp = []
        temp.append(music_list_df.iloc[i[0]].track_name)
        temp.append(music_list_df.iloc[i[0]].spotify_link)
        temp.append(music_list_df.iloc[i[0]].image_link)

        recommended_music.append(temp)
    return recommended_music


def random_music():
    rindex = np.array(sample(xrange(len(music_list_df)), 5))

    # get 10 random rows from df
    random_songs = []
    random_songs = [music_list_df.iloc[rindex].track_name] + [music_list_df.iloc[rindex].spotify_link] + [
        music_list_df.iloc[rindex].image_link]

    return random_songs


# res = recommend('mohabbat bhi jhoothi')
# print(res)


st.title('Music Recommender')

# for image,song in zip(image_link,song_link):
#     st.markdown(f'''
#     <a href="{song}">
#         <img src="{image}" width=200 />
#     </a>''',
#             unsafe_allow_html=True
#             )
#
# st.image(image_link, width=100, caption=track_name)


tab1, tab2 = st.tabs(["RECOMMEND MUSIC", "RANDOM MUSIC"])

with tab1:

    st.header("RECOMMEND ME")

    selected_music_name = st.selectbox(
        'Choose your music !!',
        music_list)

    if st.button('Play'):
        music_index = music_list_df[music_list_df['track_name'] == selected_music_name].index[0]
        temp = []
        temp.append(selected_music_name)
        temp.append(music_list_df.iloc[music_index].spotify_link)
        temp.append(music_list_df.iloc[music_index].image_link)
        st.write("[listen to](%s)" %temp[1] + "  " +temp[0])
        st.image(temp[2])

    if st.button('Recommend'):
        reccommendations = recommend(selected_music_name)

        rcol1, rcol2, rcol3, col4, col5 = st.columns(5)

        with rcol1:
            st.write("[listen to](%s)"%reccommendations[0][1]+ "  "+reccommendations[0][0])
            st.image(reccommendations[0][2])
        with rcol2:
            st.write("[listen to](%s)" % reccommendations[1][1] + "  " + reccommendations[1][0])
            st.image(reccommendations[1][2])
        with rcol3:
            st.write("[listen to](%s)" % reccommendations[2][1] + "  " + reccommendations[2][0])
            st.image(reccommendations[2][2])
        with col4:
            st.write("[listen to](%s)" % reccommendations[3][1] + "  " + reccommendations[3][0])
            st.image(reccommendations[3][2])
        with col5:
            st.write("[listen to](%s)" % reccommendations[4][1] + "  " + reccommendations[4][0])
            st.image(reccommendations[4][2])

with tab2:
    st.header("Start Listening")
    if st.button('Random'):
        random_songs = random_music()

        track_name = []
        for name in random_songs[0]:
            track_name.append(name)

        song_link = []
        for link in random_songs[1]:
            song_link.append(link)

        image_link = []
        for link in random_songs[2]:
            image_link.append(link)

        for image, song, name in zip(image_link, song_link, track_name):
            st.markdown(f'''
                       <div>
                            <a href="{song}">
                                <p float = "right" style = "text-transform:uppercase; font-size: 35px; text-decoration: none">
                                <img align="top" alt="Light" src="{image}" width="400px" >
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{name}
                                </p>
                            </a>
                       </div>''',
                        unsafe_allow_html=True
                        )
