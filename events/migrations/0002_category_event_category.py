# Generated by Django 5.1.2 on 2024-10-13 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Music', 'Music'), ('Sports', 'Sports'), ('Arts', 'Arts'), ('Food', 'Food'), ('Drinks', 'Drinks'), ('Charity', 'Charity'), ('Education', 'Education'), ('Business', 'Business'), ('Tech', 'Tech'), ('Other', 'Other')], default='Other', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.category'),
        ),
    ]
