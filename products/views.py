from django.shortcuts import render, get_object_or_404 # 10.5 import get_object_or_404
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

# 10.1
def product_detail(request, product_id): #10.2 Add the product.id as parameter
    """ A view to show product details """
    
    # 10.3 get one product based on id
    product = get_object_or_404(Product, pk=product_id)

    # 10.4 make the product available for the template by adding this to the context
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)