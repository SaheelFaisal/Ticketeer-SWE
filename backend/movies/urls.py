from django.urls import path
from .views import MovieListCreateAPIView, MovieDetailView, ReviewDetailAPIView, ReviewListCreateAPIView, MovieListView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('<int:id>/', MovieDetailView.as_view(), name='movie-detail'),
    path('<int:movie_id>/reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
