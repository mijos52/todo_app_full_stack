from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)


def __str__(self):
    """string representation of the model i think"""
    return self.title


class Meta:
    """Used to order how the tasks are retrived"""
    ordering = ["complete"]
