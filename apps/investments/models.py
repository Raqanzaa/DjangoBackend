from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Investment(models.Model):
    class InvestmentType(models.TextChoices):
        STOCK = 'ST', _('Stock')
        BOND = 'BO', _('Bond')
        MUTUAL_FUND = 'MF', _('Mutual Fund')
        ETF = 'ET', _('ETF')
        CRYPTO = 'CR', _('Cryptocurrency')
        REAL_ESTATE = 'RE', _('Real Estate')
        OTHER = 'OT', _('Other')
    
    name = models.CharField(max_length=100)
    investment_type = models.CharField(max_length=2, choices=InvestmentType.choices)
    symbol = models.CharField(max_length=10, blank=True)
    initial_investment = models.DecimalField(max_digits=12, decimal_places=2)
    current_value = models.DecimalField(max_digits=12, decimal_places=2)
    purchase_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def profit_loss(self):
        return self.current_value - self.initial_investment
    
    def profit_loss_percentage(self):
        if self.initial_investment > 0:
            return (self.profit_loss() / self.initial_investment) * 100
        return 0
    
    def __str__(self):
        return f"{self.name} - {self.current_value}"