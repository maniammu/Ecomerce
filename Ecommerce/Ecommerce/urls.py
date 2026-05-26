from django.contrib import admin
from django.urls import path
from ecom_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('add_product/', views.add_product),
    path('products/', views.products),
    path('about/', views.about),
    path('cart/', views.cart),
    path('products/', views.products_view, name='products'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
]