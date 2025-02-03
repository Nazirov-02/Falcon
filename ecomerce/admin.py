from django.contrib import admin

# Register your models here.
from .models import Category, Product, Img

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ProductImageInline(admin.TabularInline):  # yoki admin.StackedInline
    model = Img
    extra = 1  # Yangi rasm qo'shish uchun boshlang'ich qator

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]  # Product bilan bog'langan rasmlarni ko'rsatish

admin.site.register(Product, ProductAdmin)