from django.db import models

from groups_management.models import DongiGroup


class Currency(models.Model):
    name = models.CharField(max_length=50)
    code_name = models.CharField(max_length=3)  # ISO 4217 Code


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    group = models.ForeignKey(DongiGroup, on_delete=models.CASCADE)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
