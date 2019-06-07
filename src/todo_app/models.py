from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=300)
    is_done = models.BooleanField(default=False)
    priority = models.TextField(default='low')
