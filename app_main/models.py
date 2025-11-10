from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()

    def __str__(self):
        return self.title


class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='tasks/files/')

    def __str__(self):
        return f"{self.task.title} - {self.file.name}"
