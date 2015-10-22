# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20151020_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'photos/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
