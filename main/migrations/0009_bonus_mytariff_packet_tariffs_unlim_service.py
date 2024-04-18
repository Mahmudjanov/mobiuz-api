# Generated by Django 4.2.5 on 2024-01-29 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_bonus_delete_mytariff_remove_service_packet_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('coin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MyTariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gb', models.IntegerField()),
                ('minute', models.CharField(max_length=100)),
                ('sms', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Packet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tariffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mb', models.IntegerField()),
                ('sms', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Unlim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.packet')),
                ('tariffs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tariffs')),
                ('unlim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.unlim')),
            ],
        ),
    ]