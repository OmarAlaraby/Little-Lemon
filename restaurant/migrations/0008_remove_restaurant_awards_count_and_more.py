# Generated by Django 4.2 on 2023-04-03 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_restaurant_facebook_link_restaurant_isntagram_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='awards_count',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='happy_customers',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='pizza_branches_count',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='staff',
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('salary', models.IntegerField(default=0)),
                ('restaurant', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=200)),
                ('number_of_visits', models.IntegerField(default=0)),
                ('restaurant', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('restaurant', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
    ]
