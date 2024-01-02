# Generated by Django 4.2.7 on 2024-01-02 16:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('date_depart', models.DateField()),
                ('date_arrivee', models.DateField()),
                ('prix', models.IntegerField()),
                ('nbr_places', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Client_voyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reservation', models.DateField()),
                ('fk_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.client')),
                ('fk_voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.voyage')),
            ],
        ),
    ]
