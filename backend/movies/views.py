from rest_framework import generics
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404


# Movie
class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

# Review
class ReviewListCreateAPIView(generics.ListCreateAPIView):
    # This will allow users to view and create reviews for a particular movie
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter reviews by movie (to display reviews for a specific movie)
        movie_id = self.kwargs.get('movie_id')
        return Review.objects.filter(movie__id=movie_id)
    
    def get_movie(self):
        # Retrieve the movie based on the 'movie_id' URL parameter
        movie_id = self.kwargs['movie_id']
        return get_object_or_404(Movie, id=movie_id)

    def perform_create(self, serializer):
        # Add the user automatically to the review when creating it
        movie = self.get_movie()
        serializer.save(movie=movie, user=self.request.user)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'