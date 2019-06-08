from django import forms

CHOICES = [
    ('high', 'High'),
    ('mid', 'Mid'),
    ('low', 'Low'),
]


class TaskForm(forms.Form):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Describe yor task'}))
    priority = forms.CharField(label='set priority', widget=forms.Select(choices=CHOICES,attrs={'id':'priority'}))
