# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from rest_framework.test import APIRequestFactory
# from rest_framework.test import APIClient
from django.test import TestCase
from .models import Quote, Item
from django.db import IntegrityError


from rest_framework.test import APIRequestFactory




class QuoteIntegrityTest(TestCase):

    def test_quoteIntegrityTest(self,):

        factory = APIRequestFactory()
        request = factory.post('/sdf/', {'title' : 'new idea'}, format='json')

        t =Quote.objects.create(name='q1', price=-50)

        integrityErrorFlag = False
        try :
            Quote.objects.create(name='q1', price=12)
        except IntegrityError:
            integrityErrorFlag = True

        self.assertTrue(integrityErrorFlag)





