# Generated by Django 5.1.5 on 2025-01-28 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Артикул')),
                ('description', models.TextField(verbose_name='Описание')),
                ('last_update', models.DateTimeField(auto_now_add=True, verbose_name='Последнее обновление')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('last_message', models.TextField(blank=True, null=True, verbose_name='Последнее сообщение')),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
            },
        ),
    ]
