from django.shortcuts import render, redirect

# Create your views here.
from .forms import ProductForm
from .models import Product

# CRUD = Create, Read, Update, Delete
# home view
def home_view(request):
    return render(request, 'invApp/home.html')
# Create view
def Product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})
   
# Read view
def Product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products': products})
# Update view
def Product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})
# Delete view
def Product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html', {'product': product})