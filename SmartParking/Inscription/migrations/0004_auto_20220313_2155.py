# Generated by Django 3.1.7 on 2022-03-13 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inscription', '0003_auto_20220313_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil',
            old_name='entreprise',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='profil',
            old_name='matricule',
            new_name='numPlate',
        ),
        migrations.RenameField(
            model_name='profil',
            old_name='typeVoiture',
            new_name='typeCar',
        ),
    ]