from django.shortcuts import render
from django.http import HttpResponse
from todo_app.models import Task


def filter_by_priority(request):
    if request.method == 'POST':
        chosen_filter = request.POST.get('filter_by_priority')
        data = Task.objects.filter(priority=chosen_filter)
        return render(request, 'todo_app/home.html', context={'data': data})
    return HttpResponse('INVALID REQUEST')
