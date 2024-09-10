from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Task, Tag
from .forms import TagForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# user module with custom Class-based views (except logout)
class CustomUserLogin(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task-list')


def custom_user_logout(request):
    logout(request)
    return redirect('login')


class CustomUserRegister(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomUserRegister, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task-list')
        return super(CustomUserRegister, self).get(*args, **kwargs)


# task module with custom Class-based views
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/detail.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'status', 'tag']
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'status', 'tag']
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('task-list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')


# tag module with Function-based views
@login_required(login_url='login')
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags/list.html', {'tags': tags})


@login_required(login_url='login')
def tag_create(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag-list')
        else:
            messages.error(request, 'Invalid data.')
    else:
        return render(request, 'tags/create.html', {'form': form})


@login_required(login_url='login')
def tag_update(request, id):
    tag = Tag.objects.get(id=id)
    if tag is not None:
        form = TagForm(instance=tag)
    else:
        return redirect('tag-list')
    
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tag-list')

    return render(request, 'tags/update.html', {'form': form})


@login_required(login_url='login')
def tag_delete(request, id):
    tag = Tag.objects.get(id=id)
    if request.method == 'POST':
        tag.delete()
        return redirect('tag-list')
    else:
        return render(request, 'tags/delete.html', {'tag': tag})
