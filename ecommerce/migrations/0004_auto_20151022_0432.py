# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0003_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='delivery_address',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='payment_method',
            field=models.CharField(default=b'', max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_discout',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default=1, to='ecommerce.Cart'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='discount_per_product',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='items',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=1, to='ecommerce.Product'),
            preserve_default=False,
        ),
    ]
