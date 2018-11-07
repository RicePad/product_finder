from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    body = models.TextField(blank=True, default='')
    url = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to="images/")
    votes_total = models.IntegerField(default=1)
    icon = models.ImageField(upload_to="images/")
    user = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('product_home')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pretty_date(self):
        return self.published_date.strftime('%b %e %Y')
