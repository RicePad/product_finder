from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),

]
