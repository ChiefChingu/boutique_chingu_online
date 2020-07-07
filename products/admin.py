from django.contrib import admin
from .models import Product, Category # 5.2

# Register your models here.
admin.site.register(Product) # 5.3
admin.site.register(Category) # 5.3