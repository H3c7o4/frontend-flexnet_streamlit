import streamlit as st
from pages.main import get_categories, get_movies_by_genres, show_movie

hide_menu = """
<style>
#MainMenu {
    visibility:hidden;
}

footer {
    visibility:visible;
}

footer:after {
  content:'Copyright © 2023: Flexnet';
  display:block;
  color:tomato;
  position:relative;
}
</style>
"""

st.markdown(hide_menu, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("movies", '../movies')
with col2:
    st.link_button("recommendations", '../recommendations')
with col3:
    st.link_button("home", '../home')

def show_categories():
    genres = get_categories()
    cat = st.selectbox("Select a category", genres)
    movies = get_movies_by_genres(category=cat, limit=100)

    col_val = [0, 0, 0]
    col1, col2, col3 = st.columns(3)
    col_dict = {'0': col1, '1': col2, '2': col3}
    for movie in movies:
        index = col_val.index(min(col_val))

        with col_dict[str(index)]:
            show_movie(movie)
            st.markdown("---")
            col_val[index] += 1


show_categories()