# Generated by Django 4.1 on 2022-10-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateTimeField(),
        ),
    ]