from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    class CategoryType(models.TextChoices):
        INCOME = 'IN', _('Income')
        EXPENSE = 'EX', _('Expense')
        TRANSFER = 'TR', _('Transfer')
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=CategoryType.choices)
    color = models.CharField(max_length=7, default='#3B82F6')  # Hex color
    icon = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ['name', 'user']
    
    def __str__(self):
        return self.name

class Account(models.Model):
    class AccountType(models.TextChoices):
        CASH = 'CA', _('Cash')
        BANK = 'BA', _('Bank Account')
        CREDIT_CARD = 'CC', _('Credit Card')
        INVESTMENT = 'IN', _('Investment')
        LOAN = 'LO', _('Loan')
        OTHER = 'OT', _('Other')
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=AccountType.choices)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, default='USD')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=200)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='incoming_transfers')
    is_transfer = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-id']
    
    def __str__(self):
        return f"{self.description} - {self.amount}"