# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ReferenceItem(models.Model):

    referenceId = models.CharField(max_length= 255, primary_key=True)
    referenceType = models.CharField(max_length= 255)

    def __str__(self):

        return self.referenceId

class PayloadItem(models.Model):

    source = models.CharField(max_length= 255)
    reportType = models.CharField(max_length= 255)
    message = models.CharField(max_length= 4000, blank=True)
    reportId = models.CharField(max_length= 255)
    referenceResourceId = models.CharField(max_length= 255)
    referenceResourceType = models.CharField(max_length= 255)

    def __str__(self):

        return str(self.id)


class SpamReportsItem(models.Model):

    id = models.CharField(max_length= 255, primary_key=True)
    source = models.CharField(max_length= 255)
    sourceIdentityId = models.CharField(max_length= 255)
    reference = models.ForeignKey(ReferenceItem, on_delete=models.CASCADE)
    state = models.CharField(max_length= 255)
    payload = models.ForeignKey(PayloadItem, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return  self.id


