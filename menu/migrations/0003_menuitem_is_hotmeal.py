# Generated by Django 4.2 on 2023-04-03 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_catigory_menuitem_catigory'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='is_hotmeal',
            field=models.BooleanField(default=False),
        ),
    ]
