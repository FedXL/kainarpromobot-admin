# Generated by Django 5.1.5 on 2025-02-05 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0006_telegrammessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegrammessage',
            name='response',
            field=models.TextField(blank=True, null=True, verbose_name='Отчет об отправке'),
        ),
    ]
