# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Customer


# Create your views here.
def index(request):
    cu = Customer(name="YAsh")
    cu.save()
    return HttpResponse("Hello, world. You're at the polls index.")
