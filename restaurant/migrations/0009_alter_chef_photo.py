# Generated by Django 4.2 on 2023-04-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_remove_restaurant_awards_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='photo',
            field=models.ImageField(default='', upload_to='testImages/%y/%m/%d'),
        ),
    ]