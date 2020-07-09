from django.urls import path

from .views import MatchAPIView, MatchDetailAPIView

urlpatterns = [
    path('matches/', MatchAPIView.as_view()),
    path('matches/<int:id>/', MatchDetailAPIView.as_view()),
]