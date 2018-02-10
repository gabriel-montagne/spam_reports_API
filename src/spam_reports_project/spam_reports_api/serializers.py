from rest_framework import serializers

from . import models

class PayloadItemSerializer(serializers.Serializer):

    source = serializers.CharField(max_length= 255)
    reportType = serializers.CharField(max_length= 255)
    message = serializers.CharField(max_length= 4000)
    reportId = serializers.CharField(max_length= 255)
    referenceResourceId = serializers.CharField(max_length= 255)
    referenceResourceType = serializers.CharField(max_length= 255)

    class Meta:
        model = models.PayloadItem
        fields = ['id', 'source', 'reportType', 'message', 'reportId', 'referenceResourceId', 'referenceResourceType']

class ReferenceItemSerializer(serializers.Serializer):
    referenceId = serializers.CharField(max_length=255)
    referenceType = serializers.CharField(max_length=255)
    class Meta:
        model = models.ReferenceItem
        fields = ['referenceId', 'referenceType']

class SpamReportItemSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=255)
    source = serializers.CharField(max_length=255)
    sourceIdentityId = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)
    reference = ReferenceItemSerializer(many=False, read_only=True)
    payload = PayloadItemSerializer(many=False, read_only=True)
    created = serializers.DateTimeField()

    class Meta:
        model = models.SpamReportsItem
        fields = ['id', 'source', 'sourceIdentityId', 'state', 'reference', 'payload', 'created']