from django import forms
from skylight.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'image_url']
