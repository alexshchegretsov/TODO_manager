from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from todo_app.models import Task


def set_priority_high(request, task_id):
    current_task_we_set_priority = get_object_or_404(Task, id=task_id)
    current_task_we_set_priority.priority = 'high'
    current_task_we_set_priority.save()
    return redirect('home_url')


def set_priority_medium(request, task_id):
    current_task_we_set_priority = get_object_or_404(Task, id=task_id)
    current_task_we_set_priority.priority = 'mid'
    current_task_we_set_priority.save()
    return redirect('home_url')


def set_priority_low(request, task_id):
    current_task_we_set_priority = get_object_or_404(Task, id=task_id)
    current_task_we_set_priority.priority = 'low'
    current_task_we_set_priority.save()
    return redirect('home_url')
