# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

class Voltage(models.Model):
    value = models.IntegerField()
    last_name = models.CharField(max_length=30)
    updated = models.DateField(null=True)

    # Do we need to keep this?
    def was_updated_recently(self):
        return self.updated >= timezone.now() - datetime.timedelta(days=1)
