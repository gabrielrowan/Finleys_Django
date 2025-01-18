from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

