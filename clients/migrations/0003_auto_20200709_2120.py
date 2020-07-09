# Generated by Django 2.2 on 2020-07-09 21:20

import clients.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20200709_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=models.SET(clients.models.get_sentinel_user), to=settings.AUTH_USER_MODEL),
        ),
    ]
