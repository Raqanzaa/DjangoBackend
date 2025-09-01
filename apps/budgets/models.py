from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.transactions.models import Category

class Budget(models.Model):
    class PeriodType(models.TextChoices):
        WEEKLY = 'WE', _('Weekly')
        MONTHLY = 'MO', _('Monthly')
        QUARTERLY = 'QU', _('Quarterly')
        YEARLY = 'YE', _('Yearly')
        CUSTOM = 'CU', _('Custom')
    
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    period = models.CharField(max_length=2, choices=PeriodType.choices, default=PeriodType.MONTHLY)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.amount}"