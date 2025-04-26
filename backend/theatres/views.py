from rest_framework import generics
from .models import Theatre, Show
from .serializers import TheatreSerializer, ShowSerializer

class TheatreListView(generics.ListAPIView):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer

class ShowListView(generics.ListAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
