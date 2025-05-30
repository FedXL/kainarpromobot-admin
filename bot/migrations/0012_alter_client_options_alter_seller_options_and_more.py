# Generated by Django 5.1.5 on 2025-02-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0011_alter_clientprofile_client_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='seller',
            options={'verbose_name': 'Покупатель', 'verbose_name_plural': 'Покупатели'},
        ),
        migrations.AlterField(
            model_name='client',
            name='present_type',
            field=models.CharField(blank=True, choices=[('25000', '25000'), ('50000', '50000')], max_length=255, null=True, verbose_name='Тип приза'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='present_type',
            field=models.CharField(blank=True, choices=[('25000', '25000')], max_length=255, null=True, verbose_name='Тип приза'),
        ),
    ]
