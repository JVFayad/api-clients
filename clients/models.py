from django.db import models
from django.core.validators import MaxValueValidator

from products.models import Product


class Client(models.Model):
    """
    Clients only have name, email and favorite products 
    """
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=50, unique=True)
    favorite_products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Reviews has a related client and a related product
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.IntegerField(
        default=0, 
        validators=[MaxValueValidator(5)])

    def __str__(self):
        return "{0} reviwed {1}".format(
            self.client.name, self.product.title) 