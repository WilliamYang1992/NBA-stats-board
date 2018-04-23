# coding: utf-8

from django.db import models


class City(models.Model):
    """城市"""
    name = models.CharField(max_length=20, unique=True, blank=False)


class Arena(models.Model):
    """场馆"""
    name = models.CharField(max_length=30, unique=True, blank=False)
    city = models.ForeignKey(City, related_name='+', on_delete=models.CASCADE)


class Team(models.Model):
    """球队"""
    name = models.CharField(max_length=30, unique=True, blank=False)
    # 球队3位字母简称
    tricode = models.CharField(max_length=3, unique=True, blank=False)
    founded = models.DateField()
    city = models.ForeignKey(City, related_name='+', on_delete=models.CASCADE)
    arena = models.ForeignKey(Arena, related_name='+', on_delete=models.CASCADE)
    owner = models.CharField(max_length=30, blank=False, null=False)
    manager = models.CharField(max_length=30, blank=False, null=False)
    coach = models.CharField(max_length=30, blank=False, null=False)
    history = models.CharField(max_length=50)
    website = models.URLField()


class Player(models.Model):
    """球员"""
    name = models.CharField(max_length=30, unique=True, blank=False)
    height = models.FloatField()
    weight = models.FloatField()
    born = models.DateField()
    come_from = models.CharField(max_length=30)
    nba_debut = models.DateField()
    years_in_nba = models.PositiveSmallIntegerField()
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)


class PlayerPreviousTeamRecord(models.Model):
    """球员之前所在球队记录"""
    season = models.CharField(max_length=7)
    players = models.ManyToManyField(Player, related_name='previous_team_records')
    team = models.ForeignKey(Team, related_name='+', on_delete=models.CASCADE)
