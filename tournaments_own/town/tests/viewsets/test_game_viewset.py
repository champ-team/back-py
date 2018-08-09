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

    def test_ceate_game(self):
        admin = UserFactory()
        self.client.force_authenticate(user=admin)
        url = reverse('game-list')
        response = self.client.post(url, data={
            'map_name': 'name_1',
            'server_name': 'server_name',
            'server_password': 'passwd',
        })
        self.assertEqual(response.status_code, 201)
        game = Game.objects.last()
        self.assertEqual(game.map_name, 'name_1')

    def test_update_game(self):
        admin = UserFactory()
        self.client.force_authenticate(user=admin)
        game = GameFactory()
        url = reverse('game-detail', kwargs={'pk': game.pk})
        response = self.client.patch(url, data={'map_name': 'new_name_1'})
        self.assertEqual(response.status_code, 200)
        game.refresh_from_db()
        self.assertEqual(game.map_name, 'new_name_1')

    def test_destory_game(self):
        admin = UserFactory()
        self.client.force_authenticate(user=admin)
        game = GameFactory()
        url = reverse('game-detail', kwargs={'pk': game.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        games = Game.objects.all()
        self.assertEqual(len(games), 0)
