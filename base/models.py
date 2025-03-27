from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200) # The title of the task, limited to 200 characters.
    description = models.TextField(null=True, blank=True) # A text field for the task's description
    complete = models.BooleanField(default=False) # A boolean field to track whether the task is complete or not
    created = models.DateTimeField(auto_now_add=True) # Automatically sets the timestamp when the task is created.
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete'] # Orders tasks by their completion status

        