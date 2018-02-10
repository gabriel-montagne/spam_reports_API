# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import serializers
from . import models
from . import permissions

# Create your views here.

class SpamReportsItemViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating and deleting spam report items."""

    serializer_class = serializers.SpamReportItemSerializer
    queryset = models.SpamReportsItem.objects.all()
    permission_classes = (permissions.UpdatePermissions, IsAuthenticatedOrReadOnly)
