from django.db import models

# Create your models here.
class MyCars(models.Model):
    ProductID = models.CharField(max_length=18)
    ProductName = models.CharField(max_length=30)
    ProductPrice = models.PositiveIntegerField()

    def __str__(self):
        return self.ProductID