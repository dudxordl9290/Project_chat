# Generated by Django 4.1.6 on 2023-02-22 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_remove_room_room_image_room_room_image1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_image1',
            new_name='room_image',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_image2',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_image3',
        ),
    ]
