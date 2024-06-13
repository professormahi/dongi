from django.db import models


class DongiGroup(models.Model):
    name = models.CharField(max_length=100)
    simplify_debts = models.BooleanField()
