from django.urls import path, include, re_path
from products import views
from django.conf.urls import url

app_name = "products"
urlpatterns = [
    path('new/', views.ProductCreateView.as_view(), name="new"),
    re_path(r'^product_detail/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product_detail'),


]
