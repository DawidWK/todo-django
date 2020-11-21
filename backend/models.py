from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=30)
    is_done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.task)[:10]