

from django.contrib import admin
from django.contrib.auth.models import User

from django.contrib import admin
from .models import Product, Img, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ImageInline(admin.TabularInline):
    model = Img

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'price', 'category',)







