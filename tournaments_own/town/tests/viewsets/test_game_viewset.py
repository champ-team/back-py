from django.urls import include, path, reverse
from tournaments_own.town.tests.factory import GameFactory
from rest_framework.test import APITestCase, URLPatternsTestCase


class GameViewSetTests(APITestCase):

    def test_create_account(self):
        game = GameFactory()
        url = reverse('game-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(game.map_name, response.data[0]['map_name'])
