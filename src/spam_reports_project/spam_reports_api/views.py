# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import JSONParser

from . import serializers
from . import models
from . import permissions

# Create your views here.

class SpamReportsItemViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating and deleting spam report items."""

    serializer_class = serializers.SpamReportItemSerializer
    queryset = models.SpamReportsItem.objects.all()
    permission_classes = (permissions.UpdatePermissions, IsAuthenticatedOrReadOnly)
    parser_classes = (JSONParser,)


    def update(self, request, pk=None):

        instance = self.get_object()
        instance.state = request.data['status']
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
