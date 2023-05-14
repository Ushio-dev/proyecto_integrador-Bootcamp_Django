from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    dni = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=155)
    price = models.FloatField(default=0)
    actual_stock = models.IntegerField(default=0)
    supplier = models.ForeignKey(
        Supplier,
        related_name="products",
        on_delete=models.CASCADE
    )
