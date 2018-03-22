# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from RPL.models import Rpl
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from RPL.serializers import RplSerializer


class RplList(generics.ListCreateAPIView):
    queryset = Rpl.objects.all()
    serializer_class = RplSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RplSerializer

    def get_queryset(self):
        return Rpl.objects.all().filter(user=self.request.user)