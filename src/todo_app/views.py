from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
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


def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('home_url')


def to_up_task(request, task_id):
    if not task_id == Task.objects.first().id:
        task_we_want_to_rise = get_object_or_404(Task, id=task_id)
        task_lower_down = Task.objects.get(id=task_id - 1)
        task_we_want_to_rise.id, task_lower_down.id = task_lower_down.id, task_we_want_to_rise.id
        task_we_want_to_rise.save()
        task_lower_down.save()
        return redirect('home_url')
    return redirect('home_url')


def to_down_task(request, task_id):
    if not task_id == Task.objects.last().id:
        task_we_want_to_lower_down = get_object_or_404(Task, id=task_id)
        task_lift_up = Task.objects.get(id=task_id + 1)
        task_lift_up.id, task_we_want_to_lower_down.id = task_we_want_to_lower_down.id, task_lift_up.id
        task_we_want_to_lower_down.save()
        task_lift_up.save()
        return redirect('home_url')
    return redirect('home_url')


def mark_done(request, task_id):
    task_we_done = get_object_or_404(Task, id=task_id)
    task_we_done.is_done = True if not task_we_done.is_done else False
    task_we_done.save()
    return redirect('home_url')


def set_priority_high(request, task_id):
    current_task_we_set_priority = get_object_or_404(Task, id=task_id)
    current_task_we_set_priority.priority = 'high'
    current_task_we_set_priority.save()
    return redirect('home_url')


def set_priority_medium(request, task_id):
    current_task_we_set_priority = get_object_or_404(Task, id=task_id)
    current_task_we_set_priority.priority = 'medium'
    current_task_we_set_priority.save()
    return redirect('home_url')


def set_priority_low(request, task_id):
    current_task_we_set_priority = get_object_or_404(Task, id=task_id)
    current_task_we_set_priority.priority = 'low'
    current_task_we_set_priority.save()
    return redirect('home_url')

# def set_priority(request, task_id):
#     if request.method == 'POST':
#         chosen_priority = request.POST.get('priority_choice')
#         print(chosen_priority)
#         task_we_change = Task.objects.get(id=task_id)
#         task_we_change.priority = chosen_priority
#         task_we_change.save()
#         print(task_we_change.priority)
#         return redirect('home_url')
#     else:
#         return HttpResponse('INVALID REQUEST')
