# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Customer
from .models import Item
from .models import Cart

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Cart)
