from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teams.urls')),
    path('', include('players.urls')),
    path('', include('tournaments.urls')),
    path('', include('matches.urls')),
]
