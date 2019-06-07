from django.forms import ModelForm, Textarea, TextInput, MultipleChoiceField
from .models import Task


class TaskForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        # self.fields['title'].label = ''
        self.fields['content'].label = ''

    class Meta:
        model = Task
        fields = ('content',)
        widgets = {'content': Textarea(attrs={'placeholder': 'Describe your task'})}
