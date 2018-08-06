from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)


class Tournament(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Game(models.Model):
    map_name = models.CharField(max_length=255)
    server_name = models.CharField(max_length=255)
    server_password = models.CharField(max_length=255)
    start_time = models.DateTimeField()


class TeamStat(models.Model):
    standing = models.TextField()


class PlayerStat(models.Model):
    kills = models.IntegerField()