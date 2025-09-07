from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Category

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        default_categories = [
            {"name": "Salary", "type": "IN", "color": "#22c55e", "icon": "💰"},
            {"name": "Bonus", "type": "IN", "color": "#16a34a", "icon": "🎉"},
            {"name": "Gift", "type": "IN", "color": "#4ade80", "icon": "🎁"},
            {"name": "Food", "type": "EX", "color": "#ef4444", "icon": "🍔"},
            {"name": "Transport", "type": "EX", "color": "#dc2626", "icon": "🚌"},
            {"name": "Shopping", "type": "EX", "color": "#f87171", "icon": "🛒"},
            {"name": "Bills", "type": "EX", "color": "#b91c1c", "icon": "💡"},
            {"name": "Bank Transfer", "type": "TR", "color": "#3b82f6", "icon": "🏦"},
        ]
        for cat in default_categories:
            Category.objects.create(user=instance, **cat)
