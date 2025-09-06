from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Category

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_default_categories(sender, instance, created, **kwargs):
    if created:  # only for new users
        default_categories = [
            {"name": "Salary", "type": "IN", "color": "#22c55e"},
            {"name": "Bonus", "type": "IN", "color": "#16a34a"},
            {"name": "Gift", "type": "IN", "color": "#4ade80"},
            {"name": "Food", "type": "EX", "color": "#ef4444"},
            {"name": "Transport", "type": "EX", "color": "#dc2626"},
            {"name": "Shopping", "type": "EX", "color": "#f87171"},
            {"name": "Bills", "type": "EX", "color": "#b91c1c"},
            {"name": "Bank Transfer", "type": "TR", "color": "#3b82f6"},
        ]
        for cat in default_categories:
            Category.objects.create(user=instance, **cat)
