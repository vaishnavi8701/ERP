# Generated by Django 3.0.7 on 2020-09-09 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20200909_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='time',
            new_name='month',
        ),
    ]
