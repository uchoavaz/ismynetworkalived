from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class Network(models.Model):
    network_name = models.CharField(
        verbose_name="Network name",
        max_length=30
    )
    ip = models.CharField(
        verbose_name="Ip",
        max_length=15)
    last_datetime_connection = models.DateTimeField(
        verbose_name="Last connection datetime", default=timezone.now)

    class Meta:
        verbose_name = (u'Network')
        verbose_name_plural = (u"Networks")

    def __str__(self):
        return self.network_name
