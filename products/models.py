from django.db import models

class Product(models.Model):
    """
    Product have title, brand, price and image
    """
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return self.title
    
    @property
    def reviewScore(self):
        reviews = self.reviews.all()
         
        return reviews.aggregate(
            models.Avg('rate')
        )['rate__avg']