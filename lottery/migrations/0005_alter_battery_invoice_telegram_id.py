# Generated by Django 5.1.5 on 2025-01-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0004_battery_invoice_telegram_id_invoicephoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battery',
            name='invoice_telegram_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Чек'),
        ),
    ]
