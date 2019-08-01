from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
#from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Match

class MatchCreateView(CreateView):
    model = Match
    template_name = 'match_new.html'
    fields = ('team_1', 'team_2', 'score_1', 'score_2', )

class MatchListView(ListView):
    model = Match
    template_name = 'match_list.html'


# class MatchDetailView(DetailView):
#     model = Club
#     template_name = 'club_detail.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(ClubDetailView, self).get_context_data(*args, **kwargs)
#         id = self.get_object()
#         context['players'] = Player.objects.filter(club=id)
#         return context
