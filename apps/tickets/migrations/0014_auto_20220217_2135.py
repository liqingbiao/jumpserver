# Generated by Django 3.1.13 on 2022-02-17 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0013_ticket_serial_num'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('date_created',), 'verbose_name': 'Comment'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ('-date_created',), 'verbose_name': 'Ticket'},
        ),
        migrations.AlterModelOptions(
            name='ticketstep',
            options={'verbose_name': 'Ticket step'},
        ),
    ]
