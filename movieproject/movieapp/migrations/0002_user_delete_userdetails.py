# Generated by Django 4.2.6 on 2023-11-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=8)),
                ('con_password', models.CharField(max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]