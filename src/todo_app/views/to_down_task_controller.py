from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from todo_app.models import Task


def to_down_task(request, task_id):
    if not task_id == Task.objects.last().id:
        task_we_want_to_lower_down = get_object_or_404(Task, id=task_id)
        task_lift_up = Task.objects.get(id=task_id + 1)
        task_lift_up.id, task_we_want_to_lower_down.id = task_we_want_to_lower_down.id, task_lift_up.id
        task_we_want_to_lower_down.save()
        task_lift_up.save()
        return redirect('home_url')
    return redirect('home_url')
