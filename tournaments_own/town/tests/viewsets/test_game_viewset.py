from django.urls import include, path, reverse
from tournaments_own.town.tests.factory import GameFactory, UserFactory, TournamentFactory
from tournaments_own.town.models import Game
from rest_framework.test import APITestCase


class GameViewSetTests(APITestCase):

    def test_index(self):
        game = GameFactory()
        url = reverse('game-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(game.map_name, response.data['results'][0]['map_name'])

    def test_index_filter(self):
        GameFactory()
        tournament = TournamentFactory()
        game = GameFactory(tournaments=[tournament])
        url = reverse('game-list')
        response = self.client.get(url, {'tournaments': tournament.pk})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(game.map_name, response.data['results'][0]['map_name'])

    def test_retrieve(self):
        game = GameFactory()
        url = reverse('game-detail', kwargs={'pk': game.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(game.map_name, response.data['map_name'])
