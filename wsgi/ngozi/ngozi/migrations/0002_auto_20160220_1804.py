# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngozi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='adult_guests',
            field=models.CharField(default=b'2', max_length=1, verbose_name=b'Adult Guests', choices=[(b'0', b'None'), (b'1', b'One'), (b'2', b'Two'), (b'3', b'Three'), (b'4', b'Four')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='child_guests',
            field=models.CharField(default=b'0', max_length=1, verbose_name=b'Children', choices=[(b'0', b'None'), (b'1', b'One'), (b'2', b'Two'), (b'3', b'Three'), (b'4', b'Four')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='message',
            field=models.TextField(max_length=4096, null=True, blank=True),
        ),
    ]
