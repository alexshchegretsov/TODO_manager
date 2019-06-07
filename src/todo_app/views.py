from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task


def home(request):
    data = Task.objects.all()
    return render(request, 'todo_app/home.html', context={'data': data})


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


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'GET':
        context = {'form': TaskForm(initial={'title': task.title, 'content': task.content})}
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


def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('home_url')


def to_up_task(request, task_id):
    if not task_id == Task.objects.first().id:
        task_we_want_to_rise = Task.objects.get(id=task_id)
        task_lower_down = Task.objects.get(id=task_id - 1)
        task_we_want_to_rise.id, task_lower_down.id = task_lower_down.id, task_we_want_to_rise.id
        task_we_want_to_rise.save()
        task_lower_down.save()
        return redirect('home_url')
    return redirect('home_url')


def to_down_task(request, task_id):
    if not task_id == Task.objects.last().id:
        task_we_want_to_lower_down = Task.objects.get(id=task_id)
        task_lift_up = Task.objects.get(id=task_id + 1)
        task_lift_up.id, task_we_want_to_lower_down.id = task_we_want_to_lower_down.id, task_lift_up.id
        task_we_want_to_lower_down.save()
        task_lift_up.save()
        return redirect('home_url')
    return redirect('home_url')

def mark_done(request, task_id):
    task_we_done = Task.objects.get(id=task_id)
    task_we_done.is_done = True if not task_we_done.is_done else False
    task_we_done.save()
    return redirect('home_url')