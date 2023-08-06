from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Cookie_stand


class Cookie_standListView(LoginRequiredMixin, ListView):
    template_name = "Cookie_stands/Cookie_stand_list.html"
    model = Cookie_stand
    context_object_name = "Cookie_stands"


class Cookie_standDetailView(LoginRequiredMixin, DetailView):
    template_name = "Cookie_stands/Cookie_stand_detail.html"
    model = Cookie_stand
    context_object_name = "Cookie_stand"


class Cookie_standUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "Cookie_stands/Cookie_stand_update.html"
    model = Cookie_stand
    fields = "__all__"


class Cookie_standCreateView(LoginRequiredMixin, CreateView):
    template_name = "Cookie_stands/Cookie_stand_create.html"
    model = Cookie_stand
    context_object_name = "Cookie_stand"
    fields = "__all__" # "__all__" for all of them


class Cookie_standDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "Cookie_stands/Cookie_stand_delete.html"
    model = Cookie_stand

    success_url = reverse_lazy("Cookie_stand_list")
