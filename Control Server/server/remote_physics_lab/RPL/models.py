# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Rpl(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
