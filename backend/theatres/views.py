from rest_framework import generics, permissions
from .models import Theatre, Show
from .serializers import TheatreSerializer, ShowSerializer
from rest_framework.response import Response

# Theatre
class TheatreListView(generics.ListAPIView):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer

class TheatreDetailView(generics.RetrieveAPIView):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer

    def retrieve(self, request, *args, **kwargs):
        theatre = self.get_object()
        shows = Show.objects.filter(theatre=theatre)
        theatre_data = self.get_serializer(theatre).data
        shows_data = ShowSerializer(shows, many=True).data

        return Response({
            "theatre": theatre_data,
            "shows": shows_data
        })
    
# Admins create a theatre
class TheatreCreateView(generics.CreateAPIView):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer
    permission_classes = [permissions.IsAdminUser]

# Admins create a show
class ShowCreateView(generics.CreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    permission_classes = [permissions.IsAdminUser]