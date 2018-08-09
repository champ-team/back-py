from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from tournaments_own.town.models import Team, TeamStat, Tournament, Game, PlayerStat
from tournaments_own.town.serializers import (
    UserSerializer, GroupSerializer, TeamSerializer,
    TeamStatSerializer, TournamentSerializer, GameSerializer,
    PlayerStatSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamStatViewSet(viewsets.ModelViewSet):
    queryset = TeamStat.objects.all()
    serializer_class = TeamStatSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class GameViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class PlayerStatViewSet(viewsets.ModelViewSet):
    queryset = PlayerStat.objects.all()
    serializer_class = PlayerStatSerializer
