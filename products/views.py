from django.shortcuts import render
from django.contrib.auth.mixins import(LoginRequiredMixin,PermissionRequiredMixin)
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView, DetailView
from products.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required




# Create your views here.

class ProductCreateView(LoginRequiredMixin, CreateView):
    fields = ("title", "body", "url", "image", "icon")
    model = Product

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ProductListView(ListView):
    context_object_name = "product_list"
    model = Product

    def get_queryset(self):
        return Product.objects.all().order_by('-votes_total')

class ProductDetailView(DetailView):
    context_object_name = "product_detail"
    model = Product

# @login_required
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))
