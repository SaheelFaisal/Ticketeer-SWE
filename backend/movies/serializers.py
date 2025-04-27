from rest_framework import serializers
from .models import Movie, Review
from theatres.models import Show

class MovieSerializer(serializers.ModelSerializer):
    shows = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genres', 'overview', 'release_date', 'runtime', 'rating', 'vote_count', 'poster_url', 'backdrop_url', 'cast', 'shows']

    def get_shows(self, obj):
        shows = obj.shows.all()
        return [
            {
                "id": show.id,
                "theatre_name": show.theatre.name,
                "start_time": show.start_time.strftime('%Y-%m-%d %H:%M'),
                "price": show.price
            }
            for show in shows
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'movie', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'movie']  # Prevent manual input for user and movie fields