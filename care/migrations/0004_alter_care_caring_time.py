# Generated by Django 3.2.13 on 2022-12-02 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0003_auto_20221202_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='care',
            name='caring_time',
            field=models.CharField(max_length=20),
        ),
    ]
