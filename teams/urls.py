from django.urls import path

from .views import TeamAPIView, TeamDetailAPIView

urlpatterns = [
    path('teams/', TeamAPIView.as_view()),
    path('teams/<int:id>/', TeamDetailAPIView.as_view()),
]