from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Goal(models.Model):
    class GoalType(models.TextChoices):
        SAVINGS = 'SA', _('Savings')
        DEBT = 'DE', _('Debt Reduction')
        INVESTMENT = 'IN', _('Investment')
        PURCHASE = 'PU', _('Major Purchase')
        OTHER = 'OT', _('Other')
    
    name = models.CharField(max_length=100)
    goal_type = models.CharField(max_length=2, choices=GoalType.choices, default=GoalType.SAVINGS)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    current_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    deadline = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def progress_percentage(self):
        if self.target_amount > 0:
            return (self.current_amount / self.target_amount) * 100
        return 0
    
    def __str__(self):
        return f"{self.name} - {self.progress_percentage():.1f}%"