# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_auto_20150110_0736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stream',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterField(
            model_name='stream',
            name='photo',
            field=models.OneToOneField(null=True, blank=True, to='items.PhotoItem'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='tweet',
            field=models.OneToOneField(null=True, blank=True, to='items.TweetItem'),
            preserve_default=True,
        ),
    ]
