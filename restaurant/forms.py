from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name' , 'email' , 'password']

        widgets = {
            'password' : forms.PasswordInput()
        }

        labels = {
            'name' : 'user name',
            'email' : 'email addresse',
        }