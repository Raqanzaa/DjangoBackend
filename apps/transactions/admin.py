from django.contrib import admin
from .models import Category, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "color", "icon", "user", "parent")
    list_filter = ("type", "user")
    search_fields = ("name", "icon")
    ordering = ("type", "name")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("description", "type", "amount", "date", "category", "user", "created_at")
    list_filter = ("type", "date", "category", "user")
    search_fields = ("description",)
    date_hierarchy = "date"
    ordering = ("-date", "-id")
