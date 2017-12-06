# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ConfigBAC(models.Model):
    key = models.TextField(max_length=200)
    keyId = models.TextField(max_length=200)
    transacction = models.TextField(choices=(("AUTH","AUTH"),("SALE","SALE")), max_length=200)
    apiUrl = models.TextField(max_length=150)
    class Meta:
        app_label = 'Config BAC'


class RequestBAC(models.Model):
    requestHash = models.TextField(max_length=200)
    amount = models.FloatField()
    orderId = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    ccnumber = models.TextField(max_length=60)
    ccexp = models.TextField(max_length=60)
    ccv = models.TextField(max_length=60)

    class Meta:
        app_label = 'Request BAC'

class ResponseBAC(models.Model):
    raw_request = models.TextField(max_length=512)
    raw_response = models.TextField(max_length=512)

    response_time = models.FloatField(help_text=("Response time in milliseconds"))

    date_created = models.DateTimeField(auto_now_add=True)
    response = models.TextField(max_length=150)
    responseText = models.TextField(max_length=60)
    authCode = models.TextField(max_length=60)
    transacctionId = models.TextField(max_length=60)
    avsresponse = models.TextField(max_length=60)
    ccvresponse = models.TextField(max_length=60)
    responseCode = models.TextField(max_length=60)
    responseHash = models.TextField(max_length=200)
    responseAmount = models.TextField(max_length=60)
    orderId = models.TextField(max_length=200)

    class Meta:
        abstract = True
        ordering = ('-date_created',)
        app_label = 'Response BAC'
