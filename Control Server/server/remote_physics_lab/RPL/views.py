# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from RPL.models import Rpl
from rest_framework import generics
from RPL.serializers import RplSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.db import models


# this needs a lot of work from the looks of it because the view doesn't
# have user or rpl as a thing
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the RPL index.")


class RplList(generics.ListCreateAPIView):
    queryset = Rpl.objects.all()
    serializer_class = RplSerializer

    def perform_create(self, serializer):
        serializer.save(rpl=self.request.rpl)

class RplDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RplSerializer

    def get_queryset(self):
        return Rpl.objects.all().filter(rpl=self.request.rpl)