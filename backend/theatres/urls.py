from django.urls import path
from .views import TheatreListView, TheatreDetailView, TheatreCreateView, ShowCreateView

urlpatterns = [
    path('theatres/', TheatreListView.as_view(), name='theatre-list'),  # List all theatres
    path('theatres/<int:pk>/', TheatreDetailView.as_view(), name='theatre-detail'),  # Get details of a single theatre
    path('theatres/create/', TheatreCreateView.as_view(), name='theatre-create'),  # Admin only: Create a new theatre
    path('shows/create/', ShowCreateView.as_view(), name='show-create'),  # Admin only: Create a new show
]