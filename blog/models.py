from django.db import models
from restaurant.models import Customer

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=40 , default='')
    published_at = models.TimeField(auto_now=True)
    publisher_text = models.TextField(default='')
    photo = models.ImageField(default='' , upload_to='testImages/%y/%m/%d')

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title