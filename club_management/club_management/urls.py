from django.contrib import admin
from django.urls import path, include
from .views import HomePageView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', HomePageView.as_view(),name='home'),
    path('clubs/', include('clubs.urls')),
    path('players/', include('players.urls')),
    path('search/', include('search.urls')),
    path('match/', include('matches.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
