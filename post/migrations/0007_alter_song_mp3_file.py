# Generated by Django 4.2.6 on 2023-10-06 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_song_mp3_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='mp3_file',
            field=models.BinaryField(),
        ),
    ]
