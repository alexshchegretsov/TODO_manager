from django.forms import ModelForm, Textarea
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'content',)
        widgets = {'content': Textarea()}
