# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Rpl(models.Model):
    id = models.IntegerField(primary_key=True)
    variables = models.CharField(max_length=30, null=True)
    values = models.IntegerField(null=True)
    currentvalue = models.FloatField(null=True)

    def __str__(self):
        return '%s %s %s' % (self.variables, self.values, self.currentvalue)

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=15, null=True)
    place = models.IntegerField(blank=True, null=True, unique=True)

    def __str__(self):
        return '%s %s' % (self.ip, self.place)
