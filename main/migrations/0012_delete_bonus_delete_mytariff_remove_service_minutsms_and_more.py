# Generated by Django 4.2.5 on 2024-01-30 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_service_minutsms'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bonus',
        ),
        migrations.DeleteModel(
            name='MyTariff',
        ),
        migrations.RemoveField(
            model_name='service',
            name='minutsms',
        ),
        migrations.RemoveField(
            model_name='service',
            name='packet',
        ),
        migrations.RemoveField(
            model_name='service',
            name='tariffs',
        ),
        migrations.RemoveField(
            model_name='service',
            name='unlim',
        ),
        migrations.DeleteModel(
            name='MinutSms',
        ),
        migrations.DeleteModel(
            name='Packet',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Tariffs',
        ),
        migrations.DeleteModel(
            name='Unlim',
        ),
    ]