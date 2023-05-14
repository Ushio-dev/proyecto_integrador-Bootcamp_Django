from django.forms import ModelForm, TextInput
from .models import Product, Supplier


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'price': 'Precio',
            'actual_stock': 'Stock Actual',
            'supplier': 'Proveedor'
        }


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'dni': 'DNI'
        }
