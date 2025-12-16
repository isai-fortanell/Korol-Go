from django import forms
from django.forms import ModelForm
from .models import *

class MakeOrder(ModelForm):
    name = forms.CharField(max_length=200, label='')
    class Meta:
        model = Order
        fields = ['name']
    
class GetWork(ModelForm):
    is_worker = forms.BooleanField( label='')
    class Meta:
        model = Client
        fields = ['is_worker']