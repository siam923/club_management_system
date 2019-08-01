from django.shortcuts import render
from django.views.generic import ListView
from players.models import Player
## For better look ups in search:
from django.db.models import Q


class SearchPlayerView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchPlayerView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            if query == "":
                return Player.objects.featured()
            return Player.objects.search(query)
        return Player.objects.featured()
