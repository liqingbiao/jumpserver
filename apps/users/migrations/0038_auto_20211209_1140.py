# Generated by Django 3.1.13 on 2021-12-09 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_user_secret_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='source',
            field=models.CharField(choices=[('local', 'Local'), ('ldap', 'LDAP/AD'), ('openid', 'OpenID'), ('radius', 'Radius'), ('cas', 'CAS'), ('saml2', 'SAML2')], default='local', max_length=30, verbose_name='Source'),
        ),
    ]
