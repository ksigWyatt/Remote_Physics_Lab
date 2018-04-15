# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


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
