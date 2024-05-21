from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from todo.models import Task, Tag
from todo.forms import TaskForm


def index(request):
    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    context = {
        "num_tasks": num_tasks,
        "num_tags": num_tags,
    }
    return render(request, "todo/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    # queryset = Task.objects.select_related("task")
    context_object_name = "task_list"
    template_name = "todo/task_list.html"


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = "todo:tag-list"


class TagUpdateView(generic.UpdateView):
    fields = "__all__"
    success_url = "todo:tag-list"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = "todo:tag-list"





