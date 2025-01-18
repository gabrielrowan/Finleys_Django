from django.urls import path
from .views import ProductListView
from .views import about_view, contact_view, ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
]