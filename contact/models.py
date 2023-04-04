from django.db import models
from restaurant.models import Restaurant , Customer


class Feedbacks(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE , default='')
    subject = models.CharField(max_length=50 , default='')
    feedback = models.TextField(default='')
    sent_at = models.TimeField(auto_now=True)
    restaurant = models.ForeignKey(Restaurant , on_delete=models.CASCADE , default='')

    def __str__(self):
        return self.customer.name