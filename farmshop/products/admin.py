from django.contrib import admin
from .models import ProductType, Product

admin.site.register(Product)
admin.site.register(ProductType)
