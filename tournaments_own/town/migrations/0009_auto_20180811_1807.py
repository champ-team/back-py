# Generated by Django 2.1 on 2018-08-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('town', '0008_auto_20180811_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(default='default.png', upload_to='team_logos/%d'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='thumbnail',
            field=models.ImageField(default='default.png', upload_to='tournament_thumbnails/%d'),
        ),
        migrations.AlterField(
            model_name='userattribute',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='user_avatars/%d'),
        ),
    ]