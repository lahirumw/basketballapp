import self as self
from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase


class TeamTestCase(APITestCase):

    def test_post(self):
        data = {"name": "denver",
                "country": "USA",
                "won": 16,
                "lost": 8,
                "matches": 24,
                "rank": 5,
                "coach": "Tom",
                "executive": "Sparkling",
                "captain": "Roger",
                "flag": "https://s3.gag.com/1.jpg",
                "players": "Jon"
                }
        response = self.client.post("/players/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)