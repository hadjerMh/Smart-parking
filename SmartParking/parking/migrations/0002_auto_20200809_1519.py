# Generated by Django 3.0.7 on 2020-08-09 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_auth', '0003_admin_profil_admin_person'),
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartparking',
            name='administ',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_auth.admin_profil'),
        ),
    ]