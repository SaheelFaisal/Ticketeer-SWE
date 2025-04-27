import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TMDb API Key
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
TMDB_BASE_URL = 'https://api.themoviedb.org/3'


# Function to fetch additional movie details (runtime, genres, and cast)
def get_movie_details(movie_id):
    # Fetch runtime, genres, and other details
    url = f"{TMDB_BASE_URL}/movie/{movie_id}"
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        movie_data = response.json()

        # Get details
        runtime = movie_data.get('runtime', None)
        genres = [genre['name'] for genre in movie_data.get('genres', [])]
        cast = fetch_movie_cast(movie_id)
        
        # Join genres and cast into comma-separated strings
        genre_str = ', '.join(genres)
        cast_str = ', '.join(cast) if cast else None

        # Additional movie data
        title = movie_data.get('title', None)
        overview = movie_data.get('overview', '')
        release_date = movie_data.get('release_date', None)
        poster_path = movie_data.get('poster_path', None)
        backdrop_path = movie_data.get('backdrop_path', None)
        vote_average = movie_data.get('vote_average', None)
        vote_count = movie_data.get('vote_count', None)

        # Build poster and backdrop URLs
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
        backdrop_url = f"https://image.tmdb.org/t/p/w500{backdrop_path}" if backdrop_path else None

        # Return all the movie details
        return {
            'runtime': runtime,
            'genres': genre_str,
            'cast': cast_str,
            'title': title,
            'overview': overview,
            'release_date': release_date,
            'poster_url': poster_url,
            'backdrop_url': backdrop_url,
            'vote_average': vote_average,
            'vote_count': vote_count,
        }
    else:
        return None

# Function to fetch movie cast details
def fetch_movie_cast(movie_id):
    url = f"{TMDB_BASE_URL}/movie/{movie_id}/credits"
    params = {
        'api_key': TMDB_API_KEY,
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        cast_data = response.json()
        cast_list = [actor['name'] for actor in cast_data.get('cast', [])]
        return cast_list[0:5]
    else:
        return []

# Function to fetch popular movies and include runtime, genres, and cast
def get_popular_movies():
    url = f"{TMDB_BASE_URL}/movie/popular"
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
        'page': 1,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        popular_movies = response.json()['results']
        
        # Add runtime, genres, and cast for each movie
        for movie in popular_movies:
            movie_id = movie['id']
            additional_details = get_movie_details(movie_id)

            if additional_details:
                # Merge the details into the movie dictionary
                movie.update(additional_details)

        return popular_movies
    else:
        return None