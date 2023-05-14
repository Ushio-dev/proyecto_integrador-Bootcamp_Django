from django.urls import path
from .views import get_products, create_product, get_suppliers, create_supplier

urlpatterns = [
    path('productos/', get_products, name='products'),
    path('productos/crear/', create_product, name='create_products'),
    path('proveedores/', get_suppliers, name='suppliers'),
    path('proveedores/crear/', create_supplier, name='create_supplier')
]