from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied # new
from players.models import Player

from .models import Club


class ClubListView(ListView):
    model = Club
    template_name = 'club_list.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ClubListView, self).get_context_data(*args, **kwargs)
        context['clubs'] = Club.objects.all().order_by('-points')
        return context

class ClubDetailView(DetailView):
    model = Club
    template_name = 'club_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ClubDetailView, self).get_context_data(*args, **kwargs)
        id = self.get_object()
        context['players'] = Player.objects.filter(club=id)
        return context

class ClubUpdateView(LoginRequiredMixin, UpdateView):
    model = Club
    fields = ('name', 'location', 'ligue',)
    template_name = 'club_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.manager != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ClubDeleteView(LoginRequiredMixin, DeleteView):
    model = Club
    template_name = 'club_delete.html'
    success_url = reverse_lazy('club_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.manager != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
