from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone



class UserAttribute(models.Model):
    avatar = models.ImageField(upload_to='user_avatars/%d', default='default.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']


class Game(models.Model):
    map_name = models.CharField(max_length=255)
    server_name = models.CharField(max_length=255)
    server_password = models.CharField(max_length=255)
    start_time = models.DateTimeField(default=timezone.now)
    tournaments = models.ManyToManyField('Tournament', blank=True)

    class Meta:
        ordering = ['-id']


class Team(models.Model):
    logo = models.ImageField(upload_to='team_logos/%d', default='default.png')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True, blank=True)
    users = models.ManyToManyField(User, blank=True)
    games = models.ManyToManyField(Game, blank=True)
    tournaments = models.ManyToManyField('Tournament', blank=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']


class Tournament(models.Model):
    thumbnail = models.ImageField(upload_to='tournament_thumbnails/%d', default='default.png')
    name = models.CharField(max_length=255)
    description = models.TextField()
    number_of_games = models.PositiveIntegerField(default=1)
    start_time = models.DateTimeField(default=timezone.now)
    teams = models.ManyToManyField(Team, blank=True)
    games = models.ManyToManyField(Game, blank=True)

    class Meta:
        ordering = ['start_time']


class TeamStat(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    standing = models.TextField()

    class Meta:
        ordering = ['-id']


class PlayerStat(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    kills = models.IntegerField()

    class Meta:
        ordering = ['-id']
