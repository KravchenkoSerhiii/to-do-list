from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    task_status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ["-create_date", "-task_status"]

    def __str__(self):
        return f"{self.content}, {self.create_date}, {self.task_status}, {self.tags}"
