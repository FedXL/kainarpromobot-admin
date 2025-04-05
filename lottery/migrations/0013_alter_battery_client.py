# Generated by Django 5.1.5 on 2025-02-07 01:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0011_alter_clientprofile_client_and_more'),
        ('lottery', '0012_alter_battery_client_alter_battery_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battery',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='battery_cli', to='bot.client', verbose_name='Клиент'),
        ),
    ]
