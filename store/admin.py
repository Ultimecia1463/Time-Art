from django.contrib import admin
from .models import Product, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'stock', 'is_active')
    list_filter = ('brand', 'is_active')
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
