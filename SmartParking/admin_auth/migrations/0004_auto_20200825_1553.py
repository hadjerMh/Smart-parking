# Generated by Django 3.0.7 on 2020-08-25 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_auth', '0003_admin_profil_admin_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_profil',
            name='adress_entreprise',
            field=models.CharField(max_length=250, verbose_name="Adresse de l'entreprise: "),
        ),
        migrations.AlterField(
            model_name='admin_profil',
            name='entreprise',
            field=models.CharField(max_length=100, verbose_name='Nom de votre entreprise: '),
        ),
        migrations.AlterField(
            model_name='admin_profil',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Numéro de téléphone: '),
        ),
    ]
