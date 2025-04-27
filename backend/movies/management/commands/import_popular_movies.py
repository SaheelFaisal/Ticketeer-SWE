import requests
from django.core.management.base import BaseCommand
from movies.models import Movie
from movies.tmdb_utils import get_popular_movies

class Command(BaseCommand):
    help = 'Fetch popular movies from TMDb and add them to the database'

    def handle(self, *args, **kwargs):
        # Fetch popular movies from TMDb
        popular_movies = get_popular_movies()

        if popular_movies:
            for movie_data in popular_movies:
                # Check if the movie is already in the database
                if not Movie.objects.filter(tmdb_id=movie_data['id']).exists():
                    # Build the poster and backdrop URLs
                    poster_path = movie_data.get('poster_path')
                    backdrop_path = movie_data.get('backdrop_path')

                    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
                    backdrop_url = f"https://image.tmdb.org/t/p/w500{backdrop_path}" if backdrop_path else None

                    # Create movie instance with additional details fetched from TMDb
                    movie = Movie.objects.create(
                        tmdb_id=movie_data['id'],
                        title=movie_data['title'],
                        overview=movie_data.get('overview', ''),
                        release_date=movie_data.get('release_date'),
                        runtime=movie_data.get('runtime'),
                        genres=movie_data.get('genres'),  # Already fetched in get_popular_movies
                        cast=movie_data.get('cast'),  # Already fetched in get_popular_movies
                        rating=movie_data.get('vote_average'),
                        vote_count=movie_data.get('vote_count'),
                        poster_url=poster_url,
                        backdrop_url=backdrop_url
                    )
                    self.stdout.write(self.style.SUCCESS(f"Movie {movie.title} added to the database."))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Movie {movie_data['title']} already exists."))
        else:
            self.stdout.write(self.style.ERROR("Failed to fetch popular movies."))
