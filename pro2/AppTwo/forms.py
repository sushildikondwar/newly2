from django import forms
from . import models
from .models import User

class MyForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'