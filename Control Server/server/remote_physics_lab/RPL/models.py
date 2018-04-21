# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Rpl(models.Model):
    variables = models.CharField(max_length=30, null=True)
    values = models.IntegerField(null=True)

    def __str__(self):
        return '%s %s' % (self.variables, self.values)

class Users(models.Model):
    ip = models.CharField(max_length=15, null=True)
    place = models.IntegerField(blank=True, null=True, unique=True)

    def __str__(self):
        return '%s %s' % (self.ip, self.place)
