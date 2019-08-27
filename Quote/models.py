# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator





class Quote(models.Model):
    name = models.CharField(max_length=50, unique=True, primary_key=True)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    def __str__(self) :
        return self.name


class Item(models.Model):
    id1 = models.IntegerField()
    name = models.CharField(max_length=50)
    quote = models.ForeignKey(Quote, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


