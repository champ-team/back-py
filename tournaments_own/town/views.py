from django.contrib.auth.models import User, Group
from django.http import HttpResponseForbidden
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from tournaments_own.town.models import Team, TeamStat, Tournament, Game, PlayerStat
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import exceptions
from django.shortcuts import get_object_or_404
from tournaments_own.town.serializers import (
    UserSerializer, TeamSerializer,
    TeamStatSerializer, TournamentSerializer, GameSerializer,
    PlayerStatSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_fields = ('name', 'tournaments')


class TeamStatViewSet(viewsets.ModelViewSet):
    queryset = TeamStat.objects.all()
    serializer_class = TeamStatSerializer


class TournamentViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    @action(methods=['post'], detail=True)
    def subscribe_team(self, request, pk=None):
        """
        data = {'team_id': int}
        """
        team = get_object_or_404(Team, pk=request.data.get('team_id', None))

        if team.owner == request.user:
           tournament = self.get_object()
           tournament.teams.add(team)
           tournament.save()
           return Response({'status': 'team is registered'})

        raise exceptions.PermissionDenied()


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_fields = ('tournaments',)


class PlayerStatViewSet(viewsets.ModelViewSet):
    queryset = PlayerStat.objects.all()
    serializer_class = PlayerStatSerializer
