import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []

    for i in movie_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie


movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

selected_movie_name=st.selectbox('Movies',movies['title'].values)

if(st.button('Recommend')):
    recommendations=recommend(selected_movie_name)
    for it in recommendations:
        st.write(it)

