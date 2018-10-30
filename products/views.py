from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ProductCreateView(TemplateView):
    template_name = "create.html"
