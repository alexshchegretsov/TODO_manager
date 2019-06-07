from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from todo_app.models import Task


def mark_done(request, task_id):
    task_we_done = get_object_or_404(Task, id=task_id)
    task_we_done.is_done = True if not task_we_done.is_done else False
    task_we_done.save()
    return redirect('home_url')
