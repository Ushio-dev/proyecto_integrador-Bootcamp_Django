from django.contrib import admin

from compra.models import Supplier, Product


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'dni')
    search_fields = ['name', 'last_name', 'dni']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'actual_stock', 'supplier', 'price')
    list_filter = ['supplier']
    search_fields =['name']