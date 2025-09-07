from django.core.exceptions import PermissionDenied
from apps.accounts.models import CustomUser


def ensure_user_exists(backend, uid, user=None, *args, **kwargs):
    """
    Ensure only existing users can login with Google.
    Do not auto-create or merge accounts.
    """
    if user:  # already matched to a social account
        return {"user": user}

    email = kwargs.get("details", {}).get("email")
    if not email:
        raise PermissionDenied("No email provided by OAuth provider.")

    try:
        existing_user = CustomUser.objects.get(email=email)
        return {"user": existing_user}
    except CustomUser.DoesNotExist:
        raise PermissionDenied("This account is not registered. Please sign up first.")

def save_profile_picture(backend, user, response, *args, **kwargs):
    """
    Social auth pipeline function to save a user's profile picture.
    This version has a more robust check for different placeholder images.
    """
    picture_url = None

    if backend.name == "google-oauth2":
        picture_url = response.get("picture")

    if picture_url:
        if 'googleusercontent.com/profile/picture' in picture_url or picture_url.endswith('/photo.jpg'):
            user.profile_picture = None
        else:
            user.profile_picture = picture_url
        
        user.save()