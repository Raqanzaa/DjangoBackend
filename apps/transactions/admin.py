from django.contrib import admin
from .models import Category, Account, Transaction
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.
    """
    list_display = ('name', 'type', 'user', 'parent')
    list_filter = ('type', 'user')
    search_fields = ('name', 'user__username')
    ordering = ('name',)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Account model.
    """
    list_display = ('name', 'type', 'balance', 'currency', 'user', 'is_active')
    list_filter = ('type', 'is_active', 'user', 'currency')
    search_fields = ('name', 'user__username')
    list_editable = ('is_active',)
    ordering = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Transaction model.
    """
    list_display = ('date', 'description', 'amount', 'category', 'account', 'user', 'is_transfer')
    list_filter = ('date', 'is_transfer', 'user', 'category')
    search_fields = ('description', 'category__name', 'account__name', 'user__username')
    ordering = ('-date',)
    
    # Use autocomplete fields for foreign keys to improve performance with large datasets
    autocomplete_fields = ('user', 'category', 'account', 'to_account')

    # Make automatically set fields read-only
    readonly_fields = ('created_at', 'updated_at')

    # Organize the form layout
    fieldsets = (
        (None, {
            'fields': ('user', 'description', 'amount', 'date')
        }),
        ('Categorization', {
            'fields': ('category', 'account')
        }),
        ('Transfer Details', {
            'classes': ('collapse',), # Make this section collapsible
            'fields': ('is_transfer', 'to_account'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )