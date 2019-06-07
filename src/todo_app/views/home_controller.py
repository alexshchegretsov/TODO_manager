from django.shortcuts import render
from todo_app.models import Task

def home(request):
    data = Task.objects.all()
    return render(request, 'todo_app/home.html', context={'data': data})