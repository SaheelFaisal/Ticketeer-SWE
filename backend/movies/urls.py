from django.urls import path
from .views import MovieListCreateAPIView, MovieDetailView, ReviewListAPIView, ReviewCreateAPIView, MovieListView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:id>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:movie_id>/reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('movies/<int:movie_id>/reviews/create/', ReviewCreateAPIView.as_view(), name='review-create'),
]
