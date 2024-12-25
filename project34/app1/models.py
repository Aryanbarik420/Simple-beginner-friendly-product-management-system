from django.db import models

# Create your models here.
class Product(models.Model):
    prodid=models.IntegerField()
    prodname=models.CharField(max_length=20)
    qty=models.IntegerField()
    price=models.IntegerField()
    