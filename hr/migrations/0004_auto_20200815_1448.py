# Generated by Django 3.0.7 on 2020-08-15 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_auto_20200815_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='leave_type',
            field=models.CharField(max_length=50),
        ),
    ]
