from django.urls import path
from .views import UserRegistrationView, LoginUserAPIView, UserProfileView, PasswordChangeView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', LoginUserAPIView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('change-password/', PasswordChangeView.as_view(), name='change-password'),
    path('forgot-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('forgot-password/wait/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
