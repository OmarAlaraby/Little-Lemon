from django.shortcuts import render
from .models import Blog

# Create your views here.
def Blog_View(request):
    context = {
        'blogs' : Blog.objects.all
    }

    return render(request , 'blog.html' , context)