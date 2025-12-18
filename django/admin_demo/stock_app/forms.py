from django import forms

from stock_app.models import Stock


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'price', 'volume', 'symbol']