from django.urls import path
from .views import MovieListCreateAPIView, MovieListView, MovieDetailView

urlpatterns = [
    path('', MovieListCreateAPIView.as_view(), name='movie-list'),
    path('<int:id>/', MovieDetailView.as_view(), name='movie-detail'),
]
