from django.forms import ModelForm, Textarea, TextInput
from .models import Task


class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['content'].label = ''

    class Meta:
        model = Task
        fields = ('title', 'content',)
        widgets = {
            'content': Textarea(attrs={'placeholder': 'Describe your task'}),
            'title': TextInput(attrs={'placeholder': 'Put some title'}),
            }
