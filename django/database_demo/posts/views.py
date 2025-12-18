from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
   # return HttpResponse("<b>Home</b>")
    return render(request, 'home.html', {'data':'Welcome to Django Database Demo'})
