from django.db import models
from tasklist.models import TaskList


class Task(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    complated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)


