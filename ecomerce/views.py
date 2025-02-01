from django.shortcuts import render

# Create your views here.
def product_list(request):
    return render(request,'ecomerce/product-list.html')

def product_detail(request):
    return render(request,'ecomerce/product-details.html')

def customers(request):
    return render(request,'ecomerce/customers.html')

def customer_detail(request):
    return render(request,'ecomerce/customer-details.html')