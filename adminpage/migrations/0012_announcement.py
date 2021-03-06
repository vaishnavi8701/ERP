# Generated by Django 3.0.7 on 2020-08-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0011_auto_20200806_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('announce_to', models.CharField(choices=[('All', 'All'), ('HR', 'Human Resource'), ('Technical', 'Technical'), ('Marketing', 'Marketing'), ('Finance', 'Finance')], default='All', max_length=20)),
                ('announce_by', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]
