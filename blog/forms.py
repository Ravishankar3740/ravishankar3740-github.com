from django import forms
from .models import *

class Detail(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    last_name=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)


    class Meta():
        model=Data
        fields=['name','last_name']
