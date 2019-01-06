from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from products import views
from products import api_views
from django.conf.urls import url

app_name = "products"
urlpatterns = [
    path('new/', views.ProductCreateView.as_view(), name="new"),
    path('<int:product_id>/', views.upvote, name='upvote'),
    re_path(r'(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product_detail'),
    path('', views.ProductListView.as_view(), name="product_list"),
    path('product-api/', api_views.ProductListAPI.as_view(), name="productlist_api"),
    path('product-api/<int:pk>', api_views.ProductDetailAPI.as_view(), name='productdetail_api'),
    path('user-api/', api_views.UserListAPI.as_view(), name="userlist_api"),
    path('user-api/<int:pk>', api_views.UserDetailAPI.as_view(), name="userdetail_api"),
    path('', api_views.api_root),


]


urlpatterns = format_suffix_patterns(urlpatterns)
