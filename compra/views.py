from django.shortcuts import render, redirect

from .forms import ProductForm, SupplierForm
from .models import Product, Supplier


# Create your views here.
def get_products(request):
    # trae todos los productos
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})


def create_product(request):
    # si el metodo no es post, renderiza el html con el formulario, en caso deque si lo sea valida y almacena en db
    form = ProductForm()

    if (request.method == 'POST'):
        form = ProductForm(request.POST)

        if (form.is_valid()):
            form.save()
            return redirect('products')

    suppliers = Supplier.objects.all()
    return render(request, 'create_product.html', {"suppliers": suppliers, "form": form})


def get_suppliers(request):
    # trae todo los proveedores
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers.html', {"suppliers": suppliers})

def create_supplier(request):
    # si el metodo no es post, renderiza el html con el formulario, en caso de que si lo sea, valida y almacena en db
    form = SupplierForm()

    if (request.method == 'POST'):
        form = SupplierForm(request.POST)

        if (form.is_valid()):
            form.save()
            return redirect('suppliers')

    suppliers = Supplier.objects.all()
    return render(request, 'create_supplier.html', {"suppliers": suppliers, "form": form})
