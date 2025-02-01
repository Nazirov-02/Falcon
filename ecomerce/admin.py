from django.contrib import admin
from django.contrib.auth.models import User

from ecomerce.models import Customer, Product

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)