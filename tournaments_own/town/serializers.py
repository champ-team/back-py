from django.contrib.auth.models import User
from tournaments_own.town.models import Team, TeamStat, Tournament, Game, PlayerStat
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username',)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class TeamStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamStat
        fields = '__all__'


class PlayerStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStat
        fields = '__all__'
