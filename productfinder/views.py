from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class ProductListView(ListView):
    context_object_name = "product_list"
    model = Product

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'products': reverse('product_home', request=request, format=format)
    })
