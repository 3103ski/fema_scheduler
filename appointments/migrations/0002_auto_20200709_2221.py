# Generated by Django 2.2 on 2020-07-09 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='appointment',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
