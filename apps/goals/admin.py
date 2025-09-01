from django.contrib import admin
from .models import Goal
from django.utils.html import format_html

# Register your models here.
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Goal model.
    """
    list_display = (
        'name',
        'user',
        'goal_type',
        'target_amount',
        'current_amount',
        'display_progress', # Displaying the custom method
        'deadline',
        'is_completed'
    )
    list_filter = ('goal_type', 'is_completed', 'user', 'deadline')
    search_fields = ('name', 'user__username')
    list_editable = ('is_completed',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-deadline',)

    # Custom method to display progress as a formatted percentage
    def display_progress(self, obj):
        progress = obj.progress_percentage()
        return f"{progress:.2f}%"
    
    display_progress.short_description = "Progress"