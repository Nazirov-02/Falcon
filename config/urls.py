
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_list',include('ecomerce.urls')),
    path('customer_list',include('customers.urls')),
    path('login',include('accounts.urls')),
path('auth/', include('social_django.urls', namespace='social')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
