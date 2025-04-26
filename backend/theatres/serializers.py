from rest_framework import serializers
from .models import Theatre, Show
from movies.serializers import MovieSerializer  # assuming you already have this

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Show
        fields = '__all__'
