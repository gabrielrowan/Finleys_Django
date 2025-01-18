from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products.html'  
    context_object_name = 'products'

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')