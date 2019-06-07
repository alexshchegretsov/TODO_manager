from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from todo_app.models import Task


def to_up_task(request, task_id):
    if not task_id == Task.objects.first().id:
        task_we_want_to_rise = get_object_or_404(Task, id=task_id)
        task_lower_down = Task.objects.get(id=task_id - 1)
        task_we_want_to_rise.id, task_lower_down.id = task_lower_down.id, task_we_want_to_rise.id
        task_we_want_to_rise.save()
        task_lower_down.save()
        return redirect('home_url')
    return redirect('home_url')
