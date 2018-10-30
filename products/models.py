from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to="images/")
    votes_total = models.IntegerField(default=1)
    icon = models.ImageField(upload_to="images/")
    hunter = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pretty_date(self):
        return self.published_date.strftime('%b %e %Y')
