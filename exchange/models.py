from django.db import models
from django.utils import timezone


class USDExchangeRate(models.Model):
    exchange_rate = models.DecimalField(max_digits=6, decimal_places=3)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'USD: {self.exchange_rate} RUB at {self.timestamp}'
