# Generated by Django 4.2.5 on 2023-11-04 06:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_remove_room_end_datetime_course_max_classes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='back_listed',
            field=models.ManyToManyField(related_name='roomsStuBack', to=settings.AUTH_USER_MODEL),
        ),
    ]