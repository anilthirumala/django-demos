from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import title

from tasks.models import Task
tasks = [
    {'title': 'Task 1', 'description': 'Task 1'},
    {'title': 'Task 2', 'description': 'Task 2'},
]
def show_tasks(request):
    print(tasks)
    return render(request,'show_tasks.html',{'tasks':tasks})

def create_task(request):
    print('create_task')
    return render(request, 'add_task.html')

def add_task(request):
    print('add task working')
    t = Task()
    if request.method == "POST":
        t.title = request.POST['title']
        t.description = request.POST['description']
        tasks.append(t)
        return redirect(show_tasks)
    else:
        return render(request, 'add_task.html')
