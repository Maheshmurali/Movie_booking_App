# Generated by Django 4.2.6 on 2023-11-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=300)),
                ('password', models.TextField(max_length=16)),
                ('con_password', models.TextField(max_length=16)),
            ],
        ),
    ]
