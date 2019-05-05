# Generated by Django 2.1.5 on 2019-04-01 14:14

from django.db import migrations, models
import django.db.models.deletion
import wagtailmarkdown.fields


class Migration(migrations.Migration):
    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('crm', '0055_invoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceGenerationSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_title',
                 models.CharField(default='Freelance python developer', help_text='Default title to use',
                                  max_length=255)),
                ('default_language',
                 models.CharField(choices=[('en', 'English'), ('de', 'German')], default='en', max_length=4)),
                ('default_unit', models.CharField(default='hour', help_text='Work unit', max_length=200)),
                ('default_vat', models.FloatField(default=19, help_text='VAT in %')),
                ('default_payment_period',
                 models.PositiveIntegerField(default=14, help_text='Amount of days for this invoice to be payed')),
                ('default_payment_address', wagtailmarkdown.fields.MarkdownField()),
                ('default_receiver_vat_id', models.CharField(help_text='VAT ID of the receiver (you)', max_length=100)),
                ('default_sender_vat_id', models.CharField(help_text='VAT ID of the sender (client)', max_length=100)),
                ('default_tax_id', models.CharField(help_text='Your local tax id', max_length=100)),
                (
                    'default_bank_account',
                    wagtailmarkdown.fields.MarkdownField(help_text='Payment bank account details')
                ),
                ('default_contact_data', wagtailmarkdown.fields.MarkdownField()),
                ('default_logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                   related_name='+', to='wagtailimages.Image')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE,
                                              to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='logo',
            field=models.ForeignKey(blank=True, help_text='Picture to use', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                    to='wagtailimages.Image'),
        ),
    ]
