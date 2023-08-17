from django.forms import ModelForm
from django.db import models
from .models import Liquor, Brand

    
class LiquorForm(ModelForm):
    class Meta:
            model = Liquor
            fields = ["name", "numberOfBottles", "brand", "description"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['numberOfBottles'].widget.attrs.update({'class':'form-control', 'min':"1"})
        self.fields['brand'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].required=False


class updateLiquorForm(ModelForm):
    class Meta:
          model = Liquor
          fields = ["numberOfBottles", "description"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numberOfBottles'].widget.attrs.update({'class':'form-control', 'min':"1"})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})