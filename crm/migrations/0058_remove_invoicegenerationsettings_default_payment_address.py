# Generated by Django 2.1.8 on 2019-04-01 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0057_auto_20190401_1443_squashed_0059_auto_20190401_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicegenerationsettings',
            name='default_payment_address',
        ),
    ]
