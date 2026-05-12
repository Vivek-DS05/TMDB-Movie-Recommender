import streamlit as st
import pickle
import requests
st.header("Movies Recommendation System")
movies = pickle.load(open('C:/Users/Sanjay Singh/OneDrive/Desktop/Streamlit/movie_list.pkl','rb'))
similarity = pickle.load(open('C:/Users/Sanjay Singh/OneDrive/Desktop/Streamlit/similarly.pkl','rb'))
movie_list = movies['title'].values
movie = st.selectbox('Choose your favourite movie',movie_list)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse = True,key = lambda x: x[1])
    recommended_movie_name = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['id']
        recommended_movie_name.append(movies.iloc[i[0]].title)
    return recommended_movie_name

if st.button("Recommend"):
    st.subheader("You'll love these movies too")
    recommended_movies = recommend(movie)
    for i in recommended_movies:
        st.write(i)
