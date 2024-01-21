import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl", 'rb'))
movies_list = movies['title'].values
similarities = pickle.load(open("similarities.pkl", 'rb'))

st.header("Movie Recommender System")
select_value = st.selectbox("Select movie from dropdown", movies_list)
recs_num = st.number_input("How many recommendations would you like?", value=5, step=1, max_value=10000)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=dc6070be2eb35ce90d5ea4ffee860ff5&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500"+poster_path
    # full_path = "https://image.tmdb.org/t/p/w500/nj01hspawPof0mJmlgfjuLyJuRN.jpg"
    return full_path


def recommend(movie, n):
    index = movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate(similarities[index])), reverse=True, key = lambda vector:vector[1])
    recommended_movies = []
    recommended_posters = []
    
    if n + 1 < 10000:
        n += 1
    else:
        n = 9999
    for i in distances[1:n]:
        movie_id = movies.iloc[i[0]].id
        print(movies.iloc[i[0]].id)
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

if st.button("Show Recommendations"):
    movie_names, movie_posters = recommend(select_value, recs_num)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        for i in range(recs_num):
            if i % 5 == 0:
                st.text(movie_names[i])
                st.image(movie_posters[i])

        # st.text(movie_names[0])
        # st.image(movie_posters[0])
    with col2:
        for i in range(recs_num):
            if i % 5 == 1:
                st.text(movie_names[i])
                st.image(movie_posters[i])
        # st.text(movie_names[1])
        # st.image(movie_posters[1])
    with col3:
        for i in range(recs_num):
            if i % 5 == 2:
                st.text(movie_names[i])
                st.image(movie_posters[i])
        # st.text(movie_names[2])
        # st.image(movie_posters[2])
    with col4:
        for i in range(recs_num):
            if i % 5 == 3:
                st.text(movie_names[i])
                st.image(movie_posters[i])
        # st.text(movie_names[3])
        # st.image(movie_posters[3])
    with col5:
        for i in range(recs_num):
            if i % 5 == 4:
                st.text(movie_names[i])
                st.image(movie_posters[i])
        # st.text(movie_names[4])
        # st.image(movie_posters[4])
