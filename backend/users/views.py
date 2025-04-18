from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # This saves the user to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Respond with the user's data

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Respond with errors if data is invalid


class LoginUserAPIView(APIView):
    def post(self, request):
        # Extract email and password from the request
        email = request.data.get("email")
        password = request.data.get("password")

        # Authenticate user using the email and password
        user = authenticate(email=email, password=password)

        if user:
            # Generate JWT token if authentication is successful
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        # If authentication fails, return an error response
        return Response({
            'error': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)