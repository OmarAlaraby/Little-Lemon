from django.urls import path
from . import views

urlpatterns = [
    path('' , views.Blog_View , name='blog_page'),
]