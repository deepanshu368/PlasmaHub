# Generated by Django 3.2 on 2021-05-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donator',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]