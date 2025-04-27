from rest_framework import generics, status
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .tmdb_utils import get_movie_details


# Movie
class MovieCreateAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        tmdb_id = request.data.get('tmdb_id')

        if not tmdb_id:
            return Response({"error": "TMDb ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if movie with the given TMDb ID already exists
        if Movie.objects.filter(tmdb_id=tmdb_id).exists():
            return Response({"error": "Movie with this TMDb ID already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch movie details using the new function
        movie_details = get_movie_details(tmdb_id)

        if not movie_details:
            return Response({"error": "Could not fetch movie details from TMDb."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the movie instance
        movie = Movie.objects.create(
            tmdb_id=tmdb_id,
            title=movie_details['title'],
            overview=movie_details['overview'],
            release_date=movie_details['release_date'],
            runtime=movie_details['runtime'],
            rating=movie_details['vote_average'],
            vote_count=movie_details['vote_count'],
            poster_url=movie_details['poster_url'],
            backdrop_url=movie_details['backdrop_url'],
            genres=movie_details['genres'],
            cast=movie_details['cast'],
        )

        # Serialize and return the response
        serializer = self.get_serializer(movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


# Review
class ReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Review.objects.filter(movie_id=movie_id)

class ReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        movie_id = self.kwargs['movie_id']
        movie = Movie.objects.get(id=movie_id)
        serializer.save(user=self.request.user, movie=movie)