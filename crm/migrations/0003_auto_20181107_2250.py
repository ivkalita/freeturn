# Generated by Django 2.0.9 on 2018-11-07 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20181107_2150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'verbose_name_plural': 'channels'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'city'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AddField(
            model_name='company',
            name='default_daily_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='crm.City'),
        ),
    ]
