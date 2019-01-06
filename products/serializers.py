from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('title', 'published_date', 'body', 'url', 'image', 'votes_total', 'icon', 'user')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'products')
