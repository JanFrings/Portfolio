from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    hight = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    position = models.CharField(max_length=100)
    team = models.CharField(max_length=100)

    passing_yards = models.IntegerField(default=0)
    passing_touchdowns = models.IntegerField(default=0)
    rushing_yards = models.IntegerField(default=0)
    rushing_touchdowns = models.IntegerField(default=0)
