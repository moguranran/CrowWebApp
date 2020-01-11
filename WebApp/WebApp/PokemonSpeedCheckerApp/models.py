from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Pokemon(models.Model):
    #名前
    name = models.TextField()
    #図鑑No
    number = models.IntegerField()
    type_1 = models.TextField()
    #特性1
    ability_1 = models.TextField()
    #特性2
    ability_2 = models.TextField()
    #夢特性
    hidden_ability = models.TextField()
    #種族値
    hp = models.IntegerField()
    attack = models.IntegerField()
    block = models.IntegerField()
    contact = models.IntegerField()
    diffence = models.IntegerField()
    speed = models.IntegerField()

class Move(models.Model):
    name = models.TextField()