# Generated by Django 3.0.7 on 2020-09-09 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_auto_20200909_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='amt',
        ),
    ]
