import streamlit as st

from pages.main import get_movies_by_genres, show_movie, get_categories, show_recommended_movies


def show_recommendation():
    st.title("Movie App Recommender")
    st.write("Welcome to our movie app recommender! Get ready for an amazing movie journey. 🍿🎬")

    st.header("Tell us your preferences")
    st.write(
        "Our app will curate personalized movie recommendations just for you. Simply select your preferred movie genre and we'll do the rest!")

    genre = st.selectbox("Select your preferred movie genre", get_categories())

    st.header("Discover new movies")
    st.write(
        "Sit back, relax, and let our magical movie recommender do its job. With our algorithm powered by pixie dust, behold as we unveil a splendid collection of movies made just for you!")

    recommendation_button = st.button("Show Recommendations")

    if recommendation_button:
        # Perform recommendation logic based on user preferences
        recommended_movies = get_movies_by_genres(genre)

        if recommended_movies:
            st.write("Here are some movie recommendations for you:")
            for movie in recommended_movies:
                show_movie(movie)
                st.markdown("---")
        else:
            st.write("Oops! It seems our movie recommendation engine is on a break. Please try again later. 🛠️")


show_recommendation()