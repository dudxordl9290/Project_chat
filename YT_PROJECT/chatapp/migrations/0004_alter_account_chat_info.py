# Generated by Django 4.0 on 2023-02-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='chat_info',
            field=models.CharField(default='정보없음.', max_length=1000),
        ),
    ]