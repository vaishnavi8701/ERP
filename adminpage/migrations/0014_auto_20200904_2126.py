# Generated by Django 3.0.7 on 2020-09-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0013_auto_20200813_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addservices',
            name='category',
            field=models.CharField(choices=[('ERP', 'ERP'), ('CRM', 'CRM'), ('Billing', 'Billing'), ('Ecommerce', 'Ecommerce'), ('HRM', 'HRM')], default='ERP', max_length=100),
        ),
    ]