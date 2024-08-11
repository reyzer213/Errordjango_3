from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Comment
from .forms import TaskForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TaskListView(ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'to_proj/templates/task_list.html'


class Task_list_Detail(DetailView):
    model = models.Task
    template_name = 'to_proj/templates/task_detail.html'
    context_object_name = 'task'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    template_name = 'to_proj/templates/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
