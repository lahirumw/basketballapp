from django.urls import path
from .views import PlayerAPIView, PlayerDetailAPIView

urlpatterns = [
    path('players/', PlayerAPIView.as_view()),
    path('players/<int:id>/', PlayerDetailAPIView.as_view()),
]