from django.urls import path

from .views import (
    PlayerListView,
    PlayerUpdateView,
    PlayerDetailView,
    PlayerDeleteView,
    PlayerCreateView,
    )

urlpatterns = [
    path('', PlayerListView.as_view(), name='player_list'),
    path('<int:pk>/edit/',
         PlayerUpdateView.as_view(), name='player_edit'),
    path('<int:pk>/delete/',
         PlayerDeleteView.as_view(), name='player_delete'),
    path('<int:pk>/',
         PlayerDetailView.as_view(), name='player_detail'),
    path('new/', PlayerCreateView.as_view(), name='player_new'),
]
