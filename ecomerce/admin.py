from itertools import count

from django.utils.html import format_html
from django.contrib import admin
# Register your models here.
from ecomerce.models import Category, Product, Img, Product_attribute, Attribute_value, Comment
from customers.models import Customers

admin.site.site_header = 'apelsin administration'
admin.site.site_title = 'Manage products'
admin.site.index_title = 'apelsin shop admin'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)



class ProductImageInline(admin.TabularInline):
    model = Img


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','name','price','discount','stock')
    search_fields = ('name','description')
    list_filter = ('category','rating')
    inlines = [ProductImageInline]
admin.site.register(Product, ProductAdmin)


@admin.register(Product_attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Attribute_value)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('product','attribute','value')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','rating','product')

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
     list_display = ('name','email','phone','address')