# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tournament
from .serializers import TournamentSerializer


class TournamentAPIView(APIView):
    def get(self, request):
        tournaments = Tournament.objects.all()
        serializer = TournamentSerializer(tournaments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TournamentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TournamentDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Tournament.objects.get(id=id)

        except Tournament.DoesNotExist:
            raise Http404

    def get(self, request, id):
        tournament = self.get_object(id)
        serializer = TournamentSerializer(tournament)
        return Response(serializer.data)

    def put(self, request, id):
        tournament = self.get_object(id)
        serializer = TournamentSerializer(tournament, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        tournament = self.get_object(id)
        tournament.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
