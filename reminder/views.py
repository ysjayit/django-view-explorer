from django.shortcuts import render, HttpResponse
from .models import Reminder
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# reminder module with basic/default Class-based views


class ReminderList(LoginRequiredMixin, ListView):
    model = Reminder


class ReminderDetail(LoginRequiredMixin, DetailView):
    model = Reminder


class ReminderCreate(LoginRequiredMixin, CreateView):
    model = Reminder
    fields = ['title', 'reminder_time', 'is_notified']
    success_url = reverse_lazy('reminder-list')


class ReminderUpdate(LoginRequiredMixin, UpdateView):
    model = Reminder
    fields = ['title', 'reminder_time', 'is_notified']
    success_url = reverse_lazy('reminder-list')


class ReminderDelete(LoginRequiredMixin, DeleteView):
    model = Reminder
    success_url = reverse_lazy('reminder-list')
