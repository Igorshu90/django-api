# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import logging




from rest_framework import viewsets
from .models import Quote,Item
from .serializers import QuoteSerializer,ItemSerializer
import logging
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError

class QuoteView(viewsets.ModelViewSet):

    logger = logging.getLogger(__name__)
    # logging.basicConfig(filename='error.logs', filemode='w')

    queryset = Quote.objects.all()

    serializer_class = QuoteSerializer


class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer