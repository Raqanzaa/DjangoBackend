from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    class CategoryType(models.TextChoices):
        INCOME = 'IN', _('Income')
        EXPENSE = 'EX', _('Expense')

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=CategoryType.choices)
    color = models.CharField(max_length=7, default='#3B82F6')
    icon = models.CharField(max_length=10, default="📂")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ['name', 'user']

    def __str__(self):
        return self.name


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        INCOME = 'IN', _('Income')
        EXPENSE = 'EX', _('Expense')

    type = models.CharField(
        max_length=2,
        choices=TransactionType.choices,
        default=TransactionType.EXPENSE
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=200, blank=True)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-id']

    def __str__(self):
        return f"{self.get_type_display()}: {self.amount} on {self.date}"
