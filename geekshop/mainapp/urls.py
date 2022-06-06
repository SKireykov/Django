from django.urls import path

from mainapp.views import products

from mainapp.views import product

app_name = 'products'

urlpatterns = [
    path('', products, name='products_hot_product'),
    path('<int:pk>', products, name='product_list'),
    path('product/<int:pk>/', product, name='product_item')
]
