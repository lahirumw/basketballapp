# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Player
from .serializers import PlayerSerializer


class PlayerAPIView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayerDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Player.objects.get(id=id)

        except Player.DoesNotExist:
            raise Http404

    def get(self, request, id):
        player = self.get_object(id)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    def put(self, request, id):
        player = self.get_object(id)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        player = self.get_object(id)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
