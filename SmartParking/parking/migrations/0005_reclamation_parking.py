# Generated by Django 3.0.7 on 2020-08-15 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_auto_20200809_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamation',
            name='parking',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='parking.smartParking'),
        ),
    ]
