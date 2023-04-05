from django.shortcuts import render
from restaurant.models import Restaurant

# Create your views here.
def About(request):
    return render(request , 'about.html' , {'Restaurant' : Restaurant.objects.first})