# Generated by Django 4.2.5 on 2023-11-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_alter_room_back_listed_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='percentage',
            field=models.CharField(default='0', max_length=4),
        ),
    ]
