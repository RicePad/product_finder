from django.shortcuts import render
from django.contrib.auth.mixins import(LoginRequiredMixin,PermissionRequiredMixin)
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from products.models import Product


# Create your views here.

class ProductCreateView(LoginRequiredMixin, CreateView):
    fields = ("title", "body", "url", "image", "icon")
    model = Product

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
