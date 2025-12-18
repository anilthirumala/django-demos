from django.shortcuts import redirect, render

from stock_app.forms import StockForm
from stock_app.models import Stock

# Create your views here.
def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stock_list.html', {'stocks': stocks})

def add_stock(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        name = request.POST.get('name')
        price = request.POST.get('price')
        volume = request.POST.get('volume')
        Stock.objects.create(symbol=symbol, name=name, price=price, volume=volume)
        return redirect('stock_list')
    else:
        form = StockForm()
    return render(request, 'add_stock.html', {'form': form})