from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    profile_picture = models.URLField(blank=True, null=True)
    social_provider = models.CharField(max_length=50, blank=True, null=True)
    social_uid = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.email