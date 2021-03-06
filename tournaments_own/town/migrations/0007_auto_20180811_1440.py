# Generated by Django 2.1 on 2018-08-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('town', '0006_auto_20180811_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='games',
            field=models.ManyToManyField(blank=True, to='town.Game'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='teams',
            field=models.ManyToManyField(blank=True, to='town.Team'),
        ),
    ]
