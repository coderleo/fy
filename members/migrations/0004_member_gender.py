# Generated by Django 2.0.2 on 2018-03-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20180301_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.NullBooleanField(choices=[(None, 'Mid'), (1, 'Male'), (2, 'Female')]),
        ),
    ]
