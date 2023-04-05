from django.db import models
from restaurant.models import Restaurant


class Services(models.Model):
    title = models.CharField(max_length=50 , default='')
    description = models.TextField(default='')
    photo = models.ImageField(upload_to='testImages/services/%y/%m/%d')
    restaurant = models.ForeignKey(Restaurant , on_delete=models.CASCADE , default='')

    def __str__(self):
        return self.title
