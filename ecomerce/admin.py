from django.utils.html import format_html
from django.contrib import admin
# Register your models here.
from .models import Category, Product, Img

admin.site.site_header = 'apelsin administration'
admin.site.site_title = 'Manage products'
admin.site.index_title = 'apelsin shop admin'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ProductImageInline(admin.TabularInline):  # yoki admin.StackedInline
    model = Img


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','name','price','discount','stock')
    search_fields = ('name','description')
    list_filter = ('category','rating')
    inlines = [ProductImageInline]
admin.site.register(Product, ProductAdmin)




@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 100px;" />', obj.image.url)
        return "No image"