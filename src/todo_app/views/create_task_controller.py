from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from todo_app.forms import TaskForm
from todo_app.models import Task


def create_task(request):
    if request.method == 'GET':
        return render(request, 'todo_app/create.html', context={'form': TaskForm()})
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Task.objects.create(**data)
            return redirect('home_url')
        else:
            errors = form.errors
            return HttpResponse(errors)
    else:
        return HttpResponse('INVALID REQUEST')