from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from todo_app.models import Task
from todo_app.forms import TaskForm


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'GET':
        context = {'form': TaskForm(initial={'content': task.content})}
        return render(request, 'todo_app/edit.html', context)
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Task.objects.filter(id=task_id).update(**data)
            return redirect('home_url')
        else:
            errors = form.errors
            return HttpResponse(errors)
    else:
        return HttpResponse('INVALID REQUEST')