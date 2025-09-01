from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import register_user, login_user, get_user_profile

# The paths here are relative to the path defined in the root urls.py
# For example, 'register/' will become '/api/auth/register/'
urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('profile/', get_user_profile, name='profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]