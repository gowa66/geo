# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pointofinterest',
            old_name='address',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='pointofinterest',
            name='city',
        ),
        migrations.RemoveField(
            model_name='pointofinterest',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 5, 12, 15, 58, 44, 636039, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
