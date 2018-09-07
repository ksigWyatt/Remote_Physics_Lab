# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics

def index(request):
    return HttpResponse("Hello, world. You're at the RPL index.")

