# Generated by Django 3.0.7 on 2020-08-06 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0008_discount_serviceid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addservices',
            old_name='serviceid',
            new_name='service_id',
        ),
        migrations.RenameField(
            model_name='discount',
            old_name='serviceid',
            new_name='service_id',
        ),
    ]
