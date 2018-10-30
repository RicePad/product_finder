from django.urls import path, include
from products import views


urlpatterns = [
    path('create/', views.ProductCreateView.as_view(), name="create")


]
