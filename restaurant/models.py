from django.db import models
from datetime import date


class Chef(models.Model):
    name = models.CharField(max_length=30 , default='')
    position = models.CharField(max_length=30 , default='')
    description = models.TextField(default='')
    photo = models.ImageField(default='' , upload_to='testImages/%y/%m/%d')
    restaurant = models.ForeignKey('Restaurant' , on_delete=models.CASCADE, default='' , related_name='chefs')

    def __str__(self):
        return self.name


class Awards(models.Model):
    name = models.CharField(max_length=50 , default='')
    date = models.DateField(default=date.today)
    restaurant = models.ForeignKey('Restaurant' , on_delete=models.CASCADE, default='' , related_name='rewards')

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200 , unique=True)
    password = models.CharField(max_length=100)
    number_of_visits = models.IntegerField(default=0)
    restaurant = models.ForeignKey('Restaurant' , on_delete=models.CASCADE, default='Restaurant.objects.first()')

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=30 , default='')
    salary = models.IntegerField(default=0)
    working_since = models.TimeField(auto_now=True)
    restaurant = models.ForeignKey('Restaurant' , on_delete=models.CASCADE, default='', related_name='staffs')
    photo = models.ImageField(upload_to='testImages/staff/%y/%m/%d', default='')

    def __str__(self):
        return self.name


class Restaurant(models.Model):

    # basic info
    name = models.CharField(max_length=30, default='')
    addresse = models.CharField(max_length=50 , default='')
    description = models.TextField(default='')
    email = models.CharField(max_length=50 , default='')
    working_hours = models.CharField(max_length=100 , default='')
    phone = models.CharField(max_length=30, default='')

    # advanced info
    facebook_link = models.CharField(max_length=200 , default='')
    isntagram_link = models.CharField(max_length=200 , default='')
    
    def __str__(self):
        return self.name
    