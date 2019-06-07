from django import forms


class TaskForm(forms.Form):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Describe yor task'}))
