# Generated by Django 3.0.7 on 2020-08-08 11:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='administrateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='smartParking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compagnie_site', models.CharField(max_length=100, null=True)),
                ('numPlaces', models.PositiveSmallIntegerField(default=30)),
                ('reserveDuration', models.DurationField(default=datetime.timedelta(seconds=1200))),
                ('parking_latitude', models.CharField(max_length=30, null=True)),
                ('parking_longitude', models.CharField(max_length=30, null=True)),
                ('distance', models.CharField(default=1, max_length=10)),
                ('administ', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parking.administrateur')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeName', models.CharField(max_length=10)),
                ('place_given_name', models.CharField(blank=True, max_length=10, null=True)),
                ('statePlace', models.BooleanField(default=False)),
                ('parking', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parking.smartParking')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R', models.BooleanField(default=False)),
                ('arrived', models.BooleanField(default=False)),
                ('number_reservation', models.PositiveSmallIntegerField(default=0)),
                ('scan_entre', models.BooleanField(default=False)),
                ('scan_out', models.BooleanField(default=False)),
                ('timeout', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('un problème au niveau du site', 'un problème au niveau du site'), ('une infraction au niveau du parking', 'une infraction au niveau du parking'), ('autre', 'autre')], default='un problème au niveau du site', max_length=100, verbose_name='Mon problème')),
                ('rec_text', models.TextField(blank=True, null=True, verbose_name='Décrivez votre problème')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='', verbose_name="insertion d'une image ou capture d'écran")),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
