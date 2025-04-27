import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TMDb API Key
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
TMDB_BASE_URL = 'https://api.themoviedb.org/3'

def fetch_movie_from_tmdb(movie_id):
    url = f'{TMDB_BASE_URL}/movie/{movie_id}'
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        return None

# Function to fetch top-rated movies
def get_popular_movies():
    url = f"{TMDB_BASE_URL}/movie/popular"
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
        'page': 1,
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()['results']
    else:
        return None
    

if __name__ == "__main__":
    movie_data_list = get_popular_movies()
    
    if movie_data_list:
        for movie_data in movie_data_list:
            print("\nFetched Movie Data:\n")
            for key, value in movie_data.items():
                print(f"{key}: {value}")
