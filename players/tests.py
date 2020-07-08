from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Player
from .serializers import PlayerSerializer


class PlayerTestCase(APITestCase):

    def setup(self):
        self.client = APIClient()
        Player.objects.create(id=1, team=1,country= 'Sri Lanka',
            birthday='1986-11-16',
            age=34,
            debut= '2012',
            experience=8,
            position= 'Center',
            shoot= 'Right',
            matches= 35,
            rank= 5,
            image ='http://s3.amazon.com/bigbucket/1.jpg')

    def test_get_all(self):
        # get API response
        response = self.client.get('/players/')
        # get data from db
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        self.assertEqual(response.data, serializer.data)
        print(response.data)
        print(serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        data = {"id": 1,
            "team": 1,
            "country": "Sri Lanka",
            "birthday": "1986-11-16",
            "age": 34,
            "debut": "2012",
            "experience": 8,
            "position": "Center",
            "shoot": "Right",
            "matches": 35,
            "rank": 5,
            "image": "http://s3.amazon.com/bigbucket/1.jpg",
            "createdDate": "2020-07-07T15:35:01.777773Z"
        }
        response = self.client.post("/players/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

