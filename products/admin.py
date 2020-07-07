from django.contrib import admin
from .models import Product, Category # 5.2

# Register your models here.

class ProductAdmin(admin.ModelAdmin): #6.2
    list_display = (
        'sku', 
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',) # 6.4

class CategoryAdmin(admin.ModelAdmin): # 6.3
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin) # 5.3 6.
admin.site.register(Category, CategoryAdmin) # 5.3 6.