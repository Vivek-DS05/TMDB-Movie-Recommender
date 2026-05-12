import streamlit as st
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from compress_pickle import load

st.header("Movies Recommendation System")
movies = pickle.load(open('movie_list.pkl', 'rb'))
vector = load('vector.pkl.gz')
movie_list = movies['title'].values
movie = st.selectbox('Choose your favourite movie', movie_list)


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movie_vector = vector[index].reshape(1, -1)
    similarity = cosine_similarity(movie_vector, vector)
    similarity_scores = similarity[0]
    distances = sorted(
        list(enumerate(similarity_scores)),
        reverse=True,
        key=lambda x: x[1]
    )
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

if st.button("Recommend"):
    st.subheader("You'll love these movies too:")
    recommended_movies = recommend(movie)
    for m in recommended_movies:
        st.write(m)