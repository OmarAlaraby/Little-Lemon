# Generated by Django 4.2 on 2023-04-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurant_email_restaurant_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('position', models.CharField(default='', max_length=30)),
                ('description', models.TextField(default='')),
            ],
        ),
    ]