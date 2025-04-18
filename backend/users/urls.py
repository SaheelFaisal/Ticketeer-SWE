from django.urls import path
from .views import UserRegistrationView, LoginUserAPIView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', LoginUserAPIView.as_view(), name='login'),
]
