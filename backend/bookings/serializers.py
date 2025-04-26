from rest_framework import serializers
from .models import Ticket
from theatres.serializers import ShowSerializer

class TicketSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    show_detail = serializers.SerializerMethodField()


    class Meta:
        model = Ticket
        fields = ['id', 'user_email', 'user_name', 'show_detail', 'num_seats', 'barcode']

    def get_user_email(self, obj):
        return obj.user.email

    def get_user_name(self, obj):
        return obj.user.get_full_name()

    def get_show_detail(self, obj):
        return {
            "movie_name": obj.show.movie.title,
            "start_time": obj.show.start_time
        }
