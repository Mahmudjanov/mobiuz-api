# Generated by Django 4.2.5 on 2024-01-30 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_minutsms_service_minutsms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='minutsms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.minutsms'),
        ),
    ]
