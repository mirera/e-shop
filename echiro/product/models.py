from itertools import product
from pyexpat import model
from django.db import models

# Create your models here.

class Product(models.Model):
    # model = Product
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_description = models.TextField()
    product_image = models.ImageField()
    slug = models.SlugField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


