# Generated by Django 4.2.5 on 2024-01-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gb', models.IntegerField()),
                ('minute', models.CharField(max_length=100)),
                ('sms', models.IntegerField()),
            ],
        ),
    ]