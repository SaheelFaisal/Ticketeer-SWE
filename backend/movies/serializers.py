from rest_framework import serializers
from .models import Movie, Review
from theatres.models import Show

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def get_shows(self, obj):
        shows = Show.objects.filter(movie=obj)
        return [
            {
                "id": show.id,
                "theatre_name": show.theatre.name,
                "start_time": show.start_time,
                "price": show.price
            }
            for show in shows
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'movie', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'movie']  # Prevent manual input for user and movie fields