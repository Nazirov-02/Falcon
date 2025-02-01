from django.shortcuts import render
from .models import Product



# Create your views here.
def product_list(request):
    products = Product.objects.prefetch_related('images').all()
    return render(request,'ecomerce/product-list.html',{'products': products})

def product_detail(request,pk):
    products = Product.objects.prefetch_related('images').get(id=pk)
    return render(request,'ecomerce/product-details.html',{'products':products})

def customers(request):
    return render(request,'ecomerce/customers.html')

def customer_detail(request):
    return render(request,'ecomerce/customer-details.html')