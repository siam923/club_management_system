from django.urls import path

from .views import (
    ClubListView,
    ClubUpdateView,
    ClubDetailView,
    ClubDeleteView,
    )

urlpatterns = [
    path('', ClubListView.as_view(), name='club_list'),
    path('<int:pk>/edit/',
         ClubUpdateView.as_view(), name='club_edit'),
    path('<int:pk>/delete/',
         ClubDeleteView.as_view(), name='club_delete'),
    path('<int:pk>/',
         ClubDetailView.as_view(), name='club_detail'),
]
