# Generated by Django 3.0.7 on 2020-09-10 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0008_auto_20200907_1908'),
        ('finance', '0007_remove_vendor_amt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_id', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('client_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('totalvalue', models.CharField(max_length=100)),
                ('amount_paid', models.CharField(max_length=100)),
                ('balance_amt', models.CharField(max_length=100)),
                ('amount_received', models.CharField(max_length=100)),
                ('next_duedate', models.DateField(auto_now_add=True)),
                ('mode_of_pay', models.CharField(max_length=100)),
                ('cheque', models.CharField(max_length=100)),
                ('cheque_date', models.DateField(auto_now_add=True)),
                ('tax', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('online_ref', models.CharField(max_length=100)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.client')),
            ],
        ),
    ]
