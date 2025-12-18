from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Dish

def add_dish(request):
    if request.method == "POST":
        Dish.objects.create(
            name=request.POST['name'],
            price=request.POST['price'],
            description=request.POST['description']
        )
        return redirect('list_dishes')
    return render(request, 'add_dish.html')

def list_dishes(request):
    dishes = Dish.objects.all()
    return render(request, 'list_dishes.html', {'dishes': dishes})

def edit_dish(request, id):
    dish = Dish.objects.get(id=id)
    if request.method == "POST":
        dish.name = request.POST['name']
        dish.price = request.POST['price']
        dish.description = request.POST['description']
        dish.save()
        return redirect('list_dishes')
    return render(request, 'edit_dish.html', {'dish': dish})

def delete_dish(request, id):
    dish = Dish.objects.get(id=id)
    dish.delete()
    return redirect('list_dishes')
