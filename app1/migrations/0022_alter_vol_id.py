# Generated by Django 4.2.7 on 2024-01-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_voyage_vol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vol',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
