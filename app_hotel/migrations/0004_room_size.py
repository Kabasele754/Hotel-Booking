# Generated by Django 4.1 on 2022-10-03 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hotel', '0003_room_blog_absact_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='size',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]