# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=30)),
                ('book_author', models.CharField(max_length=50)),
                ('book_price', models.CharField(max_length=10)),
                ('book_section', models.CharField(max_length=10)),
            ],
        ),
    ]
