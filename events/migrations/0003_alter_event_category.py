# Generated by Django 5.1.2 on 2024-10-13 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_category_event_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Music', 'Music'), ('Sports', 'Sports'), ('Arts', 'Arts'), ('Food', 'Food'), ('Drinks', 'Drinks'), ('Charity', 'Charity'), ('Education', 'Education'), ('Business', 'Business'), ('Tech', 'Tech'), ('Other', 'Other')], default='Other', max_length=100),
        ),
    ]
