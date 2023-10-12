import json
import requests
import streamlit as st

@st.cache_data
def get_films(skip: int):
    for index in range(1, skip + 1):
        movie_list = []
        url = f'https://flexnet-backend-nboddrddha-uc.a.run.app/movies/?skip={index}&limit=10'
        response = requests.get(url, [])
        if response.status_code == 200:
            response = json.loads(response.text)
            movie_list += response
    return movie_list

@st.cache_data
def get_categories():
    url = 'https://flexnet-backend-nboddrddha-uc.a.run.app/movies/genres'
    response = requests.get(url, None)
    if response.status_code == 200:
        response = json.loads(response.text)
        return response['Genres']
    return None

@st.cache_data
def get_movies_by_genres(category: str, limit: int = 10):
    list_of_movies = []
    for skip in range(limit):
        url = f'https://flexnet-backend-nboddrddha-uc.a.run.app/movies/{category}?skip={skip}&limit=30'
        response = requests.get(url, None)
        if response.status_code != 200:
            break
        movies = json.loads(response.text)
        movies = movies[f'Movies from {category} category']
        for movie in movies:
            if movie in list_of_movies:
                continue
            else:
                list_of_movies.append(movie)
    return list_of_movies

@st.cache_data
def get_recommendations_by_movies(title: str):
    title.replace(' ', '%20')
    url = f'https://flexnet-backend-nboddrddha-uc.a.run.app/movies/recommend/{title}'
    response = requests.get(url, None)
    if response.status_code == 200:
        movie_list = json.loads(response.text)
        return movie_list
    return None

def show_movie(movie: dict) -> None:
    title = movie["original_title"]
    description = movie["overview"]
    image_url = 'https://image.tmdb.org/t/p/w500' + movie['poster_path']
    stars = round(movie['vote_average'])
    st.image(image_url, caption=title, use_column_width=True)
    st.markdown(f"### Title:")
    st.write(title)
    st.markdown("### Description :")
    st.write(description)
    st.write("🌟" * stars + f" {stars}/10")

@st.cache_data
def show_recommended_movies(title: str):
    movies = get_recommendations_by_movies(title)
    st.title(f"Recommended movies based on: {title}")

    for movie in movies:
        show_movie(movie)




def main():
    st.title('FLEXNET : Movie recommender system')
    st.image('./images/logo-SC-i69Mdz6-transformed.png')
    # Page title and description
    st.write("Welcome to our movie app recommender! Discover new movies based on your preferences.")

    # User input section
    st.header("Tell us your preferences")
    genre = st.selectbox("Select your preferred movie genre", get_categories())
    rating = st.slider("Select your preferred movie rating", min_value=1, max_value=5, step=1)

    # Generate movie recommendations
    st.header("Discover new movies")
    recommendation_button = st.button("Show Recommendations")

    limit = 10
    if recommendation_button:
        # Perform recommendation logic based on user preferences
        # Display recommended movies
        st.write("Here are some movie recommendations for you:")
        movies = get_movies_by_genres(category=genre, limit=limit)
        for movie in movies:
            st.title(movie['original_title'])
            st.text(movie['overview'])
            st.image('https://image.tmdb.org/t/p/w500' + movie['poster_path'])
    next = st.button('next')
    if next:
        limit = limit + 10
        movies = get_movies_by_genres(category=genre, limit=limit)
        for movie in movies:
            st.title(movie['original_title'])
            st.text(movie['overview'])
            st.image('https://image.tmdb.org/t/p/w500' + movie['poster_path'])

    # Additional sections
    st.header("About")
    st.write("Provide some information about your app and its features.")

    st.header("Contact")
    st.write("Include contact information for users to reach out.")


def show_home_page():
    # Add content for the home page
    st.header("Welcome to the Movie App Recommender!")
    st.write("This is the home page content.")

def show_movies_page():
    # Add content for the movies page
    st.header("Movies")
    st.write("This is the movies page content.")

def show_about_page():
    # Add content for the about page
    st.header("About")
    st.write("This is the about page content.")


def landing_page():
    st.title("🎥 Flexnet: Movie 🎞️ App Recommender")

    st.markdown("""
    ## The Smart Way To Pick A Movie

    We all love movies, but choosing what to watch next can be quite the challenge.
    Endlessly scrolling through streaming platforms, browsing trailers on YouTube,
    and searching for IMDb ratings can quickly turn into a frustrating and time-consuming task.
    If this sounds all too familiar, then you've come to the right place!

    Flexnet is here to simplify your movie selection process.
    Say goodbye to the endless search for the perfect flick, because Flexnet streamlines 
    your film choices like never before.
    """)
    st.write("")
    st.write("")

    # Create a container to hold the navigation elements
    nav_container = st.container()
    with nav_container:
        # Create a sidebar for navigation links
        st.sidebar.title("Navigation")
        # Add your navigation links as buttons or text
        home_button = st.sidebar.button("Home")
        movies_button = st.sidebar.button("Movies")
        about_button = st.sidebar.button("About")

        st.sidebar.markdown(
            """
            <style>
            .sidebar .button {
                background-color: #f5f5f5;
                color: #000000;
                margin-bottom: 10px;
                padding: 10px;
                border-radius: 5px;
                font-size: 16px;
                text-align: center;
            }
            .sidebar .button:hover {
                background-color: #dddddd;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    # Show different content based on the selected navigation
    if home_button:
        show_home_page()
    elif movies_button:
        show_movies_page()
    elif about_button:
        show_about_page()

    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("Trying to find a good film to watch friday night ?")
        st.write("Our movie app recommender is your trusty companion for all your movie nights."
                 "Let us be your movie genie, granting your cinematic wishes with the finest selection"
                 "of movies from across the known universe. 🎥✨")

    with col2:
        st.image(
            "https://img.freepik.com/free-photo/medium-shot-woman-sitting-couch_23-2149145027.jpg?size=626&ext=jpg&ga=GA1.1.1007278716.1697018521&semt=ais",
            caption="Movie Nigth", use_column_width=True)

    st.write("\n\n")

    st.markdown("""
    ## Get ready for an amazing movie journey. 🍿🎬
    """)
    st.image(
        "https://img.freepik.com/free-photo/man-watching-movie-streaming-service_23-2149026105.jpg?size=626&ext=jpg&ga=GA1.1.1007278716.1697018521&semt=ais")
    st.write("")
    st.markdown("""
    ## Sit back, relax, and let our magical movie recommender do its job.

    With our algorithm powered by TMDB API, behold as we unveil a splendid collection of movies made just for you!
             """)
    st.write("")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("""
        ## From the amazing adventures of Harry Potter in Hogwarts School of Witchcraft and Wizardry
        """)

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1551269901-5c5e14c25df7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8aGFycnklMjBwb3R0ZXJ8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
            caption="Harry Potter", use_column_width=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(
            "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202307/rs_1200x1200-230525111638-1200.margot-robbie-ryan-gosling-barbie-movie-sixteen_nine.jpeg?VersionId=xADkGye5_LkWqMD8fhHeOPhc841Sx3bd&size=690:388",
            caption="Barbie, starring Margot Robbie and Ryan Gosling, released in theatres on July 21.",
            use_column_width=True)
    with col2:
        st.markdown("""
        ## To the wonderful and pinkfull world of Barbie
        """)