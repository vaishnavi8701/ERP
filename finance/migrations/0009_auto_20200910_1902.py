# Generated by Django 3.0.7 on 2020-09-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='client_id',
            field=models.CharField(max_length=100),
        ),
    ]
