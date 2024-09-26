import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

st.title('Decentralized Movie Recommendation System')

# Function to load pickle files
def load_pickle(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error(f"Error: {filename} not found. Please make sure the file is in the correct directory.")
        st.stop()
    except Exception as e:
        st.error(f"An error occurred while loading {filename}: {str(e)}")
        st.stop()

# Load the data
st.write("Loading data...")
movies_dict = load_pickle('movies_dict.pkl')
similarity = load_pickle('similarity.pkl')

# Convert the dictionary to a DataFrame
movies = pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index = movies[movies['movie title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]]['movie title'])
    return recommended_movies

st.write("Data loaded successfully!")

movie_list = movies['movie title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommendations = recommend(selected_movie)
    st.write("Here are your top 5 movie recommendations:")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")

st.sidebar.title("About")
st.sidebar.info(
    "This decentralized movie recommendation system offers several advantages over centralized systems:\n\n"
    "1. Privacy: Your viewing history and preferences remain on your device, not on a central server.\n\n"
    "2. Personalization: Recommendations are tailored to your unique tastes without being influenced by global trends.\n\n"
    "3. Offline Access: Once the initial data is downloaded, you can get recommendations without an internet connection.\n\n"
    "4. No Filter Bubble: Avoid echo chambers created by centralized algorithms that might limit your exposure to diverse content.\n\n"
    "5. Control: You have full control over your data and can easily understand how recommendations are generated.\n\n"
    "Example: Netflix's centralized system might recommend popular shows to everyone, while this system focuses solely on your preferences, potentially surfacing hidden gems you'll love."
)