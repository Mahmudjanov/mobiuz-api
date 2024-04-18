# Generated by Django 4.2.5 on 2024-01-29 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_unlim_rename_name_service_extraservice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tariffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mb', models.IntegerField()),
                ('sms', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Tariff',
            new_name='MyTariff',
        ),
        migrations.RemoveField(
            model_name='service',
            name='extraservice',
        ),
        migrations.RemoveField(
            model_name='service',
            name='minutsms',
        ),
        migrations.RemoveField(
            model_name='service',
            name='mobicinema',
        ),
        migrations.RemoveField(
            model_name='service',
            name='packet',
        ),
        migrations.RemoveField(
            model_name='service',
            name='rouming',
        ),
        migrations.RemoveField(
            model_name='service',
            name='tariff',
        ),
        migrations.RemoveField(
            model_name='service',
            name='ussd',
        ),
        migrations.AddField(
            model_name='service',
            name='tariffs',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='main.tariffs'),
            preserve_default=False,
        ),
    ]
