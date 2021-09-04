# Generated by Django 3.2.6 on 2021-09-04 00:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210903_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmcode',
            name='code',
            field=models.CharField(default='652811', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='confirmcode',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 4, 1, 0, 50, 51585, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='code',
            field=models.CharField(default='PII4U0', max_length=255, unique=True),
        ),
    ]
