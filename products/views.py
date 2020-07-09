from django.shortcuts import render
from .models import Product # 7.2

# Create your views here.

# 7.1
def all_products(request):
    """ A view to show all products, including sorting and search queries """
    
    # 7.3 grab all products from the database and put it in products
    products = Product.objects.all() 

    # 7.4 make the products available for the template by adding this to the context
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)