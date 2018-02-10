from rest_framework import serializers

from . import models

class PayloadSerializer(serializers.Serializer):

    class Meta:
        model = models.PayloadItem
        fields = ['id', 'source', 'reportType', 'message', 'reportId', 'referenceResourceId', 'referenceResourceType']

class ReferenceItem(serializers.Serializer):

    class Meta:
        model = models.ReferenceItem
        fields = ['referenceId', 'referenceType']

class SpamReportSerializer(serializers.Serializer):

    class Meta:
        model = models.PayloadItem
        fields = ['id', 'source', 'source', 'reference', 'state', 'payload', 'created']