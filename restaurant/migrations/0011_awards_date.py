# Generated by Django 4.2 on 2023-04-03 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_staff_working_since'),
    ]

    operations = [
        migrations.AddField(
            model_name='awards',
            name='date',
            field=models.TimeField(auto_now=True),
        ),
    ]
