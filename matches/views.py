from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Match
from .serializers import MatchSerializer


class MatchAPIView(APIView):
    def get(self, request):
        matches = Match.objects.all()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MatchDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Match.objects.get(id=id)

        except Match.DoesNotExist:
            raise Http404

    def get(self, request, id):
        match = self.get_object(id)
        serializer = MatchSerializer(match)
        return Response(serializer.data)

    def put(self, request, id):
        match = self.get_object(id)
        serializer = MatchSerializer(match, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        match = self.get_object(id)
        match.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
