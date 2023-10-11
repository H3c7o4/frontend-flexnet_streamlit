import streamlit as st
from pages.main import get_categories, get_movies_by_genres

st.link_button("movies", '../movies')

def show_categories():
    genres = get_categories()
    cat = st.selectbox("Select a category", genres)
    movies = get_movies_by_genres(category=cat, limit=10)
    for i, movie in enumerate(movies):
        title = movie["original_title"]
        description = movie["overview"]
        image_url = 'https://image.tmdb.org/t/p/w500' + movie['poster_path']

        films_par_ligne = 3
        if i % films_par_ligne == 0:
            col1, col2, col3 = st.columns(films_par_ligne)

        with col1, col2, col3:
            st.image(image_url, width=150, caption=title)

        # Afficher le titre
        with col1, col2, col3:
            st.write(title)

        # Afficher la description
        with col1, col2, col3:
            st.text(description)

        # Ajouter une séparation entre les films
        if (i + 1) % films_par_ligne != 0:
            st.markdown("---")


show_categories()