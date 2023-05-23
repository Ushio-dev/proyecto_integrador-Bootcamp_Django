from django.forms import ModelForm, TextInput, Select
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
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            }),
            'actual_stock': TextInput(attrs={
                'class': 'form-control',
            }),
            'supplier': Select()

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
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
            }),
            'dni': TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            }),

        }
