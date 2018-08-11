from django.urls import include, path, reverse
from tournaments_own.town.tests.factory import GameFactory, UserFactory
from tournaments_own.town.models import Game
from rest_framework.test import APITestCase


class GameViewSetTests(APITestCase):

    def test_index_games(self):
        game = GameFactory()
        url = reverse('game-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(game.map_name, response.data[0]['map_name'])

    def test_retrieve_game(self):
        game = GameFactory()
        url = reverse('game-detail', kwargs={'pk': game.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(game.map_name, response.data['map_name'])
