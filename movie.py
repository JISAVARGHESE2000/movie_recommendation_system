import pickle
import spacy
import streamlit as st
import pandas as pd

# ------------------------------
# Functions
# ------------------------------

def recommend_movies(movie_name, movie_dictionary, n=5):
    if movie_name in movie_dictionary:
        temp = {}
        overview = movie_dictionary[movie_name]
        for i in movie_dictionary:
            if i != movie_name:
                temp[i] = overview.similarity(movie_dictionary[i])
        res = sorted(temp.items(), key=lambda a: a[1], reverse=True)
        return list(dict(res[:n]).keys())
    else:
        return []

def get_high_quality_image(url, width=600, height=900):
    if "UX" in url:
        url = url.replace("UX67", f"UX{width}")
    if "UY" in url:
        url = url.replace("UY98", f"UY{height}")  
    if "CR" in url:
        url = url.replace("CR0,0,67,98", f"CR0,0,{width},{height}")
        url = url.replace("CR2,0,67,98", f"CR2,0,{width},{height}")
    return url

# ------------------------------
# Streamlit App UI
# ------------------------------

st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.title("🎬 Movie Recommendation System")
st.markdown("Get top movie recommendations based on **overview similarity**!")

# Load data once into session_state
if 'movie_dictionary' not in st.session_state:
    df = pd.read_csv('imdb_top_1000.csv')
    with open('file.pkl', 'rb') as obj1:
        dict1 = pickle.load(obj1)
    st.session_state['movie_dictionary'] = dict1
    st.session_state['df'] = df

# UI layout
st.markdown("### Choose a movie to get recommendations")
movie = st.selectbox('🎥 Select a movie:', sorted(st.session_state['movie_dictionary'].keys()))
button = st.button("🔍 Show Recommendations")

if movie and button:
    st.subheader("📽️ Top Recommendations")
    recommendations = recommend_movies(movie, st.session_state['movie_dictionary'])
    
    if recommendations:
        rec_df = st.session_state['df'][st.session_state['df']['Series_Title'].isin(recommendations)]
        cols = st.columns(5)
        for idx, row in rec_df.iterrows():
            with cols[recommendations.index(row['Series_Title']) % 5]:
                st.image(get_high_quality_image(row['Poster_Link']), use_column_width=True)
                st.caption(f"**{row['Series_Title']}** ({row['Released_Year']})")
    else:
        st.warning("Movie not found in the dictionary!")
