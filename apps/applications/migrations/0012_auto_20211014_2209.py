# Generated by Django 3.1.13 on 2021-10-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0011_auto_20210826_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(blank=True, db_index=True, max_length=128, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='username',
            field=models.CharField(blank=True, db_index=True, max_length=128, verbose_name='Username'),
        ),
    ]
