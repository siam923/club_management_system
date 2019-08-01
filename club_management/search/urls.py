from django.urls import path

from . import views

app_name='search'

urlpatterns = [
    path('', views.SearchPlayerView.as_view(), name='query'),
]
