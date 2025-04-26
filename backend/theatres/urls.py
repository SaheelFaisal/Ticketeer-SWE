from django.urls import path
from .views import TheatreListView, ShowListView

urlpatterns = [
    path('theatres/', TheatreListView.as_view(), name='theatre-list'),
    path('shows/', ShowListView.as_view(), name='show-list'),
]
