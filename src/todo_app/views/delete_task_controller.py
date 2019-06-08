from django.shortcuts import redirect
from todo_app.models import Task


def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    for new_id, task in enumerate(Task.objects.all(), start=1):
        task.update_id(new_id)

    return redirect('home_url')
