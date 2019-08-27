# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Quote.models import Quote, Item
# Register your models here.
admin.site.register(Quote)
admin.site.register(Item)
