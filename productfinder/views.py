from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from products.models import Product

class ProductListView(ListView):
    context_object_name = "product_list"
    model = Product
