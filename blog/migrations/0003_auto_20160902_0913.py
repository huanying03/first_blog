# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
