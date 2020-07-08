# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Team
from .serializers import TeamSerializer


class TeamAPIView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Team.objects.get(id=id)

        except Team.DoesNotExist:
            raise Http404

    def get(self, request, id):
        team = self.get_object(id)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def put(self, request, id):
        team = self.get_object(id)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        team = self.get_object(id)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
