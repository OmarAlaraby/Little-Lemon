# Generated by Django 4.2 on 2023-04-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='email',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='working_hours',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
