from django.urls import path
from . import views

urlpatterns = [
    path('' , views.View_Services , name = 'services_page')
]
