from django.contrib import admin
from .models import Product, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Allows adding new items directly in the admin interface


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "status", "created_at"]  # Updated list_display
    list_filter = ["status", "created_at"]
    search_fields = ["user__username", "user__email"]
    inlines = [OrderItemInline]  # Include OrderItem inlines


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "unit", "price", "stock"]
    search_fields = ["name", "unit"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
