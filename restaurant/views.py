from django.shortcuts import render , redirect
from .models import Restaurant

def Home(request):
    context = {
        'Restaurant' : Restaurant.objects.first,
    }

    return render(request , 'home.html' , context)