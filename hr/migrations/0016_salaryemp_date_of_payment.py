# Generated by Django 3.0.7 on 2020-09-07 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0015_auto_20200907_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='salaryemp',
            name='date_of_payment',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
