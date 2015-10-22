# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_auto_20151022_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='delivery_name',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
    ]
