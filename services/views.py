from django.shortcuts import render
from .models import Services

def View_Services(request):
    
    context = {
        'services' : Services.objects.all()
    }
    
    return render(request , 'services.html' , context)
