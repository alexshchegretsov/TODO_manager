from django.db import models

# Create your models here.
class Task(models.Model):
    # title = models.CharField(max_length=125)
    content = models.CharField(max_length=300)
    is_done = models.BooleanField(default=False)
    priority = models.TextField(blank=True)


