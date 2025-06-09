
import streamlit as st
import pandas as pd
import pickle

# Load the processed data and similarity matrix
movies, similarity = pickle.load(open('movie_data.pkl', 'rb'))

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended = []
    for i in distances[1:6]:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

# UI with Streamlit
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox("Choose a movie", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write("### Recommended Movies:")
    for i in recommendations:
        st.write(i)
