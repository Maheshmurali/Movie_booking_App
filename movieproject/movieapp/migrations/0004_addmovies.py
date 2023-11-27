# Generated by Django 4.2.6 on 2023-11-26 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_userdetails_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddMovies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieName', models.CharField(max_length=100)),
                ('movieYear', models.IntegerField(null=True)),
                ('movieSummary', models.TextField(max_length=300)),
                ('poster', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]