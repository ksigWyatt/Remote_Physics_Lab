# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Current(models.Model):
    value = models.IntegerField()
    last_name = models.CharField(max_length=30)
    updated = models.DateField(null=True)