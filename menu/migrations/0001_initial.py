# Generated by Django 4.2 on 2023-04-03 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0007_restaurant_facebook_link_restaurant_isntagram_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.TextField(default='')),
                ('price', models.IntegerField(default=0)),
                ('photo', models.ImageField(default='', upload_to='')),
                ('restaurant', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
    ]