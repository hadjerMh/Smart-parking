# Generated by Django 3.0.7 on 2020-08-09 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parking', '0003_delete_administrateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartparking',
            name='administ',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
