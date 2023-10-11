import streamlit as st
from pages.main import get_films, show_movie

def show_movies_page(skip: int):
    movies = get_films(skip)
    col_val = [0, 0, 0]
    col1, col2, col3 = st.columns(3)
    col_dict = {'0': col1, '1': col2, '2': col3}

    for movie in movies:
        index = col_val.index(min(col_val))

        with col_dict[str(index)]:
            show_movie(movie)
            # st.markdown("---")
            col_val[index] += 1

def show_next_movies_page(debut: int, limit: int):
    for i in range(debut, limit):
        show_movies_page(i)

show_movies_page(1)
show_movies_page(2)
show_movies_page(3)
