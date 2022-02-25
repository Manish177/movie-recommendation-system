import streamlit as st
import pickle
import requests

movies = pickle.load(open('data/movie_list.pkl', 'rb'))
df = pickle.load(open('data/df.pkl', 'rb'))
similarity = pickle.load(open('data/similarity.pkl', 'rb'))

def movie_path(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?api_key=83de9c633dd050d1b248697933702574"
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    poster_path='https://image.tmdb.org/t/p/original/'+poster_path
    return poster_path

def recommend(movie):
    index = df[df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    lst1=[]
    lst2=[]
    for i in distances[1:6]:
        lst1.append(df.iloc[i[0]].title)
        lst2.append(df.iloc[i[0]].id)
    return lst1, lst2

st.title('Movie Recommender System')
option = st.selectbox(
     'Select the Movie',
     movies)
st.write('You selected:', option)
# if st.button('Recommend'):
recommended_movies, ids = recommend(option)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.write(recommended_movies[0])
    st.image(movie_path(ids[0]))

with col2:
    st.write(recommended_movies[1])
    st.image(movie_path(ids[1]))

with col3:
    st.write(recommended_movies[2])
    st.image(movie_path(ids[2]))

with col4:
    st.write(recommended_movies[3])
    st.image(movie_path(ids[3]))

with col5:
    st.write(recommended_movies[4])
    st.image(movie_path(ids[4]))


st.write('All film related data used including poster art is supplied by [The Movie Database (TMDb)](https://www.themoviedb.org/)')

st.image('tmdb_logo.png')