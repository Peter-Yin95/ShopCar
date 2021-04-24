from django.db import models

# Create your models here.
class ProductDetail(models.Model):
    ProductID = models.CharField(max_length=18)
    ProductName = models.CharField(max_length=30)
    ProductPrice = models.PositiveIntegerField()
    ProductNumber = models.PositiveIntegerField(default=100)
    ProductOffer = models.CharField(max_length=30)

    def __str__(self):
        return self.ProductID