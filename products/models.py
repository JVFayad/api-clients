from django.db import models

class Product(models.Model):
    """
    Product have title, brand, price and image
    """
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.FileField(upload_to="product/images/")

    def __str__(self):
        return self.title
    