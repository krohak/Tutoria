# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
