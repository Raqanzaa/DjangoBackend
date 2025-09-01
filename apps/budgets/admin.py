from django.contrib import admin
from .models import Budget
from django.utils.html import format_html

# Register your models here.
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Budget model.
    """
    list_display = ('name', 'user', 'category', 'amount', 'period', 'start_date', 'is_active')
    list_filter = ('period', 'is_active', 'user', 'category')
    search_fields = ('name', 'user__username', 'category__name')
    list_editable = ('is_active',)
    ordering = ('-start_date',)
    
    autocomplete_fields = ('user', 'category')

    fieldsets = (
        (None, {
            'fields': ('name', 'user', 'category', 'amount')
        }),
        ('Period and Status', {
            'fields': ('period', 'start_date', 'end_date', 'is_active')
        }),
    )
