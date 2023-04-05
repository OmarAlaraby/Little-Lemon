from django.shortcuts import render
from .models import MenuItem


def Menu(request):

    context = {
        'menu' : MenuItem.objects.all()
    }

    return render(request , 'menu.html' , context)