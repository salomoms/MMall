# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('birth_date', models.DateField()),
                ('password', models.TextField()),
                ('gender', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_by',
            field=models.ForeignKey(to='ecommerce.Customer'),
        ),
    ]
