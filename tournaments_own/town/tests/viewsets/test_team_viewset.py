from django.urls import include, path, reverse
from tournaments_own.town.tests.factory import TeamFactory
from tournaments_own.town.models import Team
from rest_framework.test import APITestCase


class GameViewSetTests(APITestCase):

    def test_index(self):
        TeamFactory()
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
