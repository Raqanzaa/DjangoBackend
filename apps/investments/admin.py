from django.contrib import admin
from .models import Investment
from django.utils.html import format_html

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Investment model.
    """
    list_display = (
        'name',
        'user',
        'investment_type',
        'current_value',
        'purchase_date',
        'display_profit_loss' # Displaying the custom method
    )
    list_filter = ('investment_type', 'user', 'purchase_date')
    search_fields = ('name', 'symbol', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-purchase_date',)

    fieldsets = (
        (None, {
            'fields': ('name', 'user', 'investment_type', 'symbol')
        }),
        ('Financials', {
            'fields': ('initial_investment', 'current_value', 'purchase_date')
        }),
        ('Additional Info', {
            'fields': ('notes', 'created_at', 'updated_at')
        }),
    )

    # Custom method to display profit/loss with color
    def display_profit_loss(self, obj):
        pl = obj.profit_loss()
        color = 'green' if pl >= 0 else 'red'
        return format_html(f'<span style="color: {color};">{pl:+.2f}</span>')
    
    display_profit_loss.short_description = "Profit/Loss"
    display_profit_loss.admin_order_field = 'current_value' # Allows sorting by this conceptual column
