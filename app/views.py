from django.views.generic.list import ListView
from .models import Todo
from django.views.generic.detail import DetailView


class TaskList(ListView):
    """Lists all the task that a user currenlty have uses listview for implementation"""

    model = Todo
    context_object_name = "tasks"  # This is for use inside the template


class TaskDetail(DetailView):
    """Show the full detail of the list"""

    model = Todo
    context_object_name = "task"
