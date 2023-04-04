from django.shortcuts import render , redirect
from django.http import HttpRequest
from .models import Restaurant , Customer
from .forms import CustomerForm
# from django.contrib.auth.forms import UserCreationForm

'''
    next step is to understand users account and how to link any form to the user 
'''

def Home(request):
    if request.method == 'POST':
        data = CustomerForm(request.POST)
        if data.is_valid():
            updated_data = data.save(commit=False)
            updated_data.restaurant = Restaurant.objects.first()
            updated_data.save()
            return redirect('')


    return render(request , 'index.html' , {'Restaurant' : Restaurant.objects.first , 'CForm' : CustomerForm })