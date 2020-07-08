from django.urls import path
from .views import TournamentAPIView, TournamentDetailAPIView

urlpatterns = [
    path('tournaments/', TournamentAPIView.as_view()),
    path('tournaments/<int:id>/', TournamentDetailAPIView.as_view()),
]