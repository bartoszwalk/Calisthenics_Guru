from django import forms
from django.forms import ModelForm
from .models import Youtuber

class YoutuberForm(ModelForm):
    class Meta:
        model = Youtuber
        fields = "__all__"

        labels = {
            'title': '',
            'description': '',
            'subscribers': '',
            'link': '',
            'image': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Youtuber Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'subscribers': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Subscribers'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'})
        }