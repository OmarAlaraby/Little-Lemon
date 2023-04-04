from django.db import models
from restaurant.models import Restaurant

class Catigory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=50 , default='')
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    photo = models.ImageField(default='' , upload_to='testImages/%y/%m/%d')
    restaurant = models.ForeignKey(Restaurant , on_delete=models.CASCADE , default='')
    catigory = models.ForeignKey(Catigory , on_delete=models.CASCADE , default='')
    is_hotmeal = models.BooleanField(default=False)

    def __str__(self):
        return self.name