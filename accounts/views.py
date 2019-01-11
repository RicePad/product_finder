from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import TemplateView, CreateView
from accounts import forms
from django.urls import reverse_lazy


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = "signup.html"
    success_url = reverse_lazy('product_home')
