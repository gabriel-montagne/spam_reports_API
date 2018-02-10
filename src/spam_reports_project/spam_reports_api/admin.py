# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ReferenceItem)
admin.site.register(models.PayloadItem)
admin.site.register(models.SpamReportsItem)