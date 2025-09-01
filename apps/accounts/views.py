from rest_framework import status, permissions
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from django.utils.translation import gettext_lazy as _
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserSerializer,
)
from django.shortcuts import redirect
from django.conf import settings
import json

@login_required # ✅ KEEP this decorator
def google_oauth_callback(request):
    """
    Handle Google OAuth callback and redirect to frontend with tokens.
    """
    print("OAuth callback received")
    
    # The @login_required decorator already ensures the user is authenticated.
    # So this 'if' statement is guaranteed to be true.
    try:
        # Generate JWT tokens for the authenticated user
        refresh = RefreshToken.for_user(request.user)
        
        # Redirect to frontend with tokens as query parameters
        frontend_url = f"http://localhost:3000/oauth-callback?refresh={str(refresh)}&access={str(refresh.access_token)}"
        print("Redirecting to:", frontend_url)
        return redirect(frontend_url)
    except Exception as e:
        print("Error generating tokens:", str(e))
        return redirect('http://localhost:3000/login?error=token_generation_failed')
    
@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user": UserSerializer(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def login_user(request):
    print("Login request data:", request.data)
    serializer = UserLoginSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user": UserSerializer(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )
    else:
        print("Serializer errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_user_profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


