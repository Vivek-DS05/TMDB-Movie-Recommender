import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity
st.header("Movies Recommendation System")
movies = pickle.load(open('movie_list.pkl','rb'))
vector = pickle.load(open('vector.pkl','rb'))
movie_list = movies['title'].values
movie = st.selectbox('Choose your favourite movie',movie_list)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movie_vector = vector[index]
    similarity = cosine_similarity([movie_vector], vector)[0]
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
