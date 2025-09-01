from django.contrib import admin
from .models import SavingsPlan
from django.utils.html import format_html

@admin.register(SavingsPlan)
class SavingsPlanAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SavingsPlan model.
    """
    # Columns to display in the list view
    list_display = (
        'name', 
        'user', 
        'target_amount', 
        'current_amount', 
        'frequency', 
        'end_date', 
        'is_active'
    )

    # Fields to allow filtering on in the right sidebar
    list_filter = (
        'is_active', 
        'frequency', 
        'user', 
        'start_date', 
        'end_date'
    )

    # Fields to include in the search bar
    # Use '__' to search on related model fields
    search_fields = (
        'name', 
        'user__username', 
        'user__email'
    )

    # Fields that should not be editable in the admin form
    readonly_fields = (
        'created_at', 
        'current_amount' # Often, current_amount is updated by transactions, not manually
    )

    # Organize the detail view form into logical sections
    fieldsets = (
        (None, {
            'fields': ('name', 'user', 'target_amount')
        }),
        ('Contribution Schedule', {
            'fields': ('frequency', 'amount_per_frequency', 'start_date', 'end_date')
        }),
        ('Status and Progress', {
            'fields': ('current_amount', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )

    # Order the list view by end date by default
    ordering = ('-end_date',)