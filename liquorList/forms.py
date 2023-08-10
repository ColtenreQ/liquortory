from django.forms import ModelForm
from django.db import models
from .models import Liquor

    
class LiquorForm(ModelForm):
    class Meta:
            model = Liquor
            fields = ["name", "numberOfBottles", "brand"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['numberOfBottles'].widget.attrs.update({'class':'form-control'})
        self.fields['brand'].widget.attrs.update({'class':'form-control'})
