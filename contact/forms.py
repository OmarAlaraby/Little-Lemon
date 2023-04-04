from django import forms
from .models import Feedbacks

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        exclude = ['restaurant' , 'customer']

        labels = {
            'name' : 'Name',
            'email' : 'Email addresse',
            'subject' : 'Subject',
            'feedback' : 'Message'
        }