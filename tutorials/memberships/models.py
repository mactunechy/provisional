from django.db import models

MEMBERSHIP_CHOICES = [
    ('free','free'),
    ('premium','premium'),
    ('enterprise','enterprise'),
]


class Membership(models.Model):
    name         = models.CharField(max_length=255,choices=MEMBERSHIP_CHOICES)
    price        = models.IntegerField()

    def __str__(self):
        return self.name

