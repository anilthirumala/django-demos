from django.shortcuts import render
from django.http import HttpResponse
from .forms import DishForm
# Create your views here.
def adddish(request):
    form = DishForm()
    return render(request,'adddish.html',{'form':form})
