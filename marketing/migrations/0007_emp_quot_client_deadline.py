# Generated by Django 3.0.7 on 2020-09-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0006_remove_emp_quot_client_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_quot',
            name='client_deadline',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]