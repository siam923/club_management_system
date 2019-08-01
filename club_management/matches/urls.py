from django.urls import path

from .views import (
    MatchCreateView,
    MatchListView,
    )

urlpatterns = [
    path('', MatchListView.as_view(), name='match_list'),
    #path('<int:pk>/',
    #     PlayerDetailView.as_view(), name='player_detail'),
    path('new/', MatchCreateView.as_view(), name='match_new'),
]
