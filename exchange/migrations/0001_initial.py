# Generated by Django 5.2.1 on 2025-06-02 11:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USDExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_rate', models.DecimalField(decimal_places=3, max_digits=6)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
