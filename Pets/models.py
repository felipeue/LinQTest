from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Owner(models.Model):
    nickname = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.nickname)


class Pet(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='pets', blank=True)
    owner = models.ForeignKey(Owner)

    def __unicode__(self):
        return unicode(self.name)
