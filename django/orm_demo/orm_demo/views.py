
from django.shortcuts import render, redirect
#from .forms import DishForm
def adddish(request):
    # if request.method == 'POST':
    #     form = DishForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('dish_list')
    # else:
    #     form = DishForm()
    return render(request, 'add_dish.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contactus.html')

