from django.urls import path
from accounts import views



urlpatterns = [
    path('login-page', views.login_page, name='login_page'),
    path('logout', views.logout_view, name='logout'),
    path('register',views.register_view, name='register'),
]