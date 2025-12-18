# dishes/forms.py
from django import forms
from .models import Dish


class DishForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    price = forms.DecimalField(label="Price")
    cuisine = forms.CharField(label="Cuise")
    description = forms.Textarea("Description")

