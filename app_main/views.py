
from django.views.generic.detail import DetailView
from .models import Task

from django.views.generic.list import ListView
from .models import Task

class HomePageView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'