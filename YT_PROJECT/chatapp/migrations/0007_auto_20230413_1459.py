# Generated by Django 3.2.16 on 2023-04-13 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0006_auto_20230412_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='room_view',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_image1',
            field=models.ImageField(null=True, upload_to='media/2023/04/13/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_image2',
            field=models.ImageField(null=True, upload_to='media/2023/04/13/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_image3',
            field=models.ImageField(null=True, upload_to='media/2023/04/13/'),
        ),
    ]