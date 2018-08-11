from django.urls import include, path, reverse
from tournaments_own.town.tests.factory import TournamentFactory, UserFactory, GameFactory, TeamFactory
from tournaments_own.town.models import Tournament, Team
from rest_framework.test import APITestCase
from rest_framework import status
import json


class TournamentViewSetTests(APITestCase):

    def test_index(self):
        tournament = TournamentFactory()
        url = reverse('tournament-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], tournament.name)

    def test_retrive(self):
        tournament = TournamentFactory()
        url = reverse('tournament-detail', kwargs={'pk': tournament.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(tournament.name, response.data['name'])

    def test_subscribe_anone(self):
        tournament = TournamentFactory()
        url = reverse('tournament-subscribe-team', kwargs={'pk': tournament.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_subscribe_not_found_team(self):
        user = UserFactory(is_superuser=False, is_staff=False)
        self.client.force_authenticate(user=user)
        tournament = TournamentFactory()
        url = reverse('tournament-subscribe-team', kwargs={'pk': tournament.pk})
        response = self.client.post(
            url,
            content_type='application/json',
            data=json.dumps({'team_id': 42})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_subscribe_not_team_owner(self):
        user = UserFactory(is_superuser=False, is_staff=False)
        team = TeamFactory()
        self.client.force_authenticate(user=user)

        tournament = TournamentFactory()
        url = reverse('tournament-subscribe-team', kwargs={'pk': tournament.pk})

        response = self.client.post(
            url,
            content_type='application/json',
            data=json.dumps({'team_id': team.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_subscribe_sucess(self):
        user = UserFactory(is_superuser=False, is_staff=False)
        team = TeamFactory(owner=user)
        self.client.force_authenticate(user=user)

        tournament = TournamentFactory()
        url = reverse('tournament-subscribe-team', kwargs={'pk': tournament.pk})

        response = self.client.post(
            url,
            content_type='application/json',
            data=json.dumps({'team_id': team.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(tournament.teams.count(), 1)
        self.assertEqual(tournament.teams.last(), team)
