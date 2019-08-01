from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Player
from clubs.models import Club

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied # new


class PlayerCreateView(LoginRequiredMixin, CreateView):
    model = Player
    template_name = 'player_new.html'
    fields = ('name', 'height', 'goals', 'assists', 'clean_sheets', )

    ## Initialize default fields
    def form_valid(self, form):
        user = self.request.user
        club = Club.objects.filter(manager=user).first()
        form.instance.club = club
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        flag = request.user.is_manager
        if not flag:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class PlayerListView(ListView):
    model = Player
    template_name = 'player_list.html'

    def get_context_data(self, **kwargs):
        context = super(PlayerListView, self).get_context_data(**kwargs)
        q = Player.objects.all().order_by('-goals')[:4]
        context['top'] = q
        return context


class PlayerDetailView(DetailView):
    model = Player
    template_name = 'player_detail.html'


class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    model = Player
    fields = ('name', 'height', 'goals', 'assists', 'clean_sheets', 'club')
    template_name = 'Player_edit.html'
    login_url = 'login'

    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj. != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class PlayerDeleteView(LoginRequiredMixin, DeleteView):
    model = Player
    template_name = 'player_delete.html'
    success_url = reverse_lazy('player_list')
    login_url = 'login'

    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)
