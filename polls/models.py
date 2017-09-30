# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Customer(models.Model):
    name = models.CharField(max_length=200)

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    time = models.DateTimeField()
    status = models.CharField(max_length=10)
    items = models.ManyToManyField(Item)
