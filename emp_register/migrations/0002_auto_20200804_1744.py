# Generated by Django 3.0.7 on 2020-08-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_loc',
            field=models.CharField(max_length=1000),
        ),
    ]
