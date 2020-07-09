# Generated by Django 2.2 on 2020-07-09 22:08

import appointments.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0006_client_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointmentDate', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('lastModified', models.DateField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.Client')),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=models.SET(appointments.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
