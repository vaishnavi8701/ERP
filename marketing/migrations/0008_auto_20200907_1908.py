# Generated by Django 3.0.7 on 2020-09-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0007_emp_quot_client_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp_quot',
            name='client_deadline',
            field=models.CharField(max_length=100),
        ),
    ]
