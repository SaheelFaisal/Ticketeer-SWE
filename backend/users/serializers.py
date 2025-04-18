from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Don't send the password back in responses.

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        # Create the user
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user
