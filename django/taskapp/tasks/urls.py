from django.urls import path
from tasks.views import show_tasks, create_task, add_task

urlpatterns = [
    path('', show_tasks, name='show_tasks'),
    path('add/', create_task, name='create_task'),
    path('save/',add_task, name='add_task'),
]