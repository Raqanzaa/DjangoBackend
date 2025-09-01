from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class SavingsPlan(models.Model):
    class FrequencyType(models.TextChoices):
        DAILY = 'DA', _('Daily')
        WEEKLY = 'WE', _('Weekly')
        MONTHLY = 'MO', _('Monthly')
        YEARLY = 'YE', _('Yearly')
    
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    current_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    frequency = models.CharField(max_length=2, choices=FrequencyType.choices, default=FrequencyType.MONTHLY)
    amount_per_frequency = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.current_amount}/{self.target_amount}"