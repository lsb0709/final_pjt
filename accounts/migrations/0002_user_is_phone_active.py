# Generated by Django 3.2.13 on 2022-12-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_phone_active',
            field=models.BooleanField(default=False),
        ),
    ]
