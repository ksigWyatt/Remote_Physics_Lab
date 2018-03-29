# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Rpl(models.Model):
    variables = models.CharField(max_length=30)
    values = models.IntegerField()
