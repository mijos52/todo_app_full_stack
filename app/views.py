from django.views.generic.list import ListView
from .models import Todo
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView


class TaskList(ListView):
    """Lists all the task that a user currenlty have uses listview for implementation"""

    model = Todo
    context_object_name = "tasks"  # This is for use inside the template


class TaskDetail(DetailView):
    """Show the full detail of the list"""

    model = Todo
    context_object_name = "task"


class TaskCreate(CreateView):
    """Create a new todo item"""

    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskUpdate(UpdateView):
    """Update an exit todo item"""

    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskDelete(DeleteView):
    """Delete an item from the todo list"""

    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("tasks")
