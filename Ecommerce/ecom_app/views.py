from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    return render(request, 'home.html')

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        type = request.POST['type']

        Product.objects.create(
            name=name,
            price=price,
            type=type
        )

        return HttpResponse("Product added successfully")

    return render(request, 'add_product.html')

def products(request):
    data = Product.objects.all()
    return render(request, 'products.html', {'products': data})

def about(request):
    return render(request, 'about.html')
def cart(request):
    return render(request, 'cart.html')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product # Or whatever your product model class is named

# Inventory Dashboard
def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

# Action Route: Deletes entry cleanly and structural routing handles redirect
def delete_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        product.delete()
    return redirect('/products/') # Instantly reloads view with object removed
