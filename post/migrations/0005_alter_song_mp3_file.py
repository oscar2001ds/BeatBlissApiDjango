# Generated by Django 4.2.6 on 2023-10-06 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_song_mp3_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='mp3_file',
            field=models.BinaryField(),
        ),
    ]
