# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('adult_guests', models.CharField(default=b'2', max_length=1, choices=[(b'0', b'None'), (b'1', b'One'), (b'2', b'Two'), (b'3', b'Three'), (b'4', b'Four')])),
                ('child_guests', models.CharField(default=b'0', max_length=1, choices=[(b'0', b'None'), (b'1', b'One'), (b'2', b'Two'), (b'3', b'Three'), (b'4', b'Four')])),
                ('entered', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(max_length=4096)),
            ],
        ),
    ]
