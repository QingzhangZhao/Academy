# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=130)),
                ('content', models.TextField()),
                ('images', models.ImageField(upload_to='./static/images/', blank=True)),
            ],
        ),
    ]
