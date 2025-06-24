from django.db import models

# Create your models here.\
class Products(models.Model):
    name = models.CharField(max_length=230)
    price=models.FloatField()
    stock= models.IntegerField()
    image_url=models.CharField()

class Offers (models.Model):
    code= models.CharField(max_length=200)
    description= models.CharField(max_length=80)
    discount= models.FloatField()