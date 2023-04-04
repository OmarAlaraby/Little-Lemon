from django.shortcuts import render , redirect
from .forms import FeedbackForm
from restaurant.models import Restaurant , Customer

'''
    next step is to understand users account and how to link any form to the user
'''

def contact(request):

    if request.method == 'POST':
        data = FeedbackForm(request.POST)
        if data.is_valid():
            updated_data = data.save(commit=False)
            updated_data.restaurant = Restaurant.objects.first()
            if Customer.objects.filter(name=request.user):
                updated_data.customer = Customer.objects.filter(name=request.user).first()
            updated_data.save()

    return render(request , 'contact.html' , {'contact_form' : FeedbackForm})