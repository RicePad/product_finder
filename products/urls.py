from django.urls import path, include
from products import views

app_name = "products"
urlpatterns = [
    path('new/', views.ProductCreateView.as_view(), name="new")


]
