# Generated by Django 2.0 on 2018-01-05 14:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180105_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_date',
            new_name='approved_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 5, 14, 8, 4, 653905, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 5, 14, 8, 4, 653905, tzinfo=utc)),
        ),
    ]
