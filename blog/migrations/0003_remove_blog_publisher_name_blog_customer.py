# Generated by Django 4.2 on 2023-04-03 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_alter_chef_photo'),
        ('blog', '0002_alter_blog_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='publisher_name',
        ),
        migrations.AddField(
            model_name='blog',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='restaurant.customer'),
        ),
    ]