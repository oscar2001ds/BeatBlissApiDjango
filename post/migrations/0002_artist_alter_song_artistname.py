# Generated by Django 4.2.6 on 2023-10-12 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=100)),
                ('artistImg', models.BinaryField()),
                ('artistDesc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='artistName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.artist'),
        ),
    ]