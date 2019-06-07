from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=125)
    content = models.CharField(max_length=300)
    # date = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    # class Meta:
    #     ordering = ['id']

    def __str__(self):
        return self.title