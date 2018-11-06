from django.urls import path, include, re_path
from products import views
from django.conf.urls import url

app_name = "products"
urlpatterns = [
    path('new/', views.ProductCreateView.as_view(), name="new"),
    path('<int:product_id>/', views.upvote, name='upvote'),
    re_path(r'(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product_detail'),
    re_path(r'(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    path('', views.ProductListView.as_view(), name="product_list"),
]
