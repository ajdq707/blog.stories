# Generated by Django 4.1.4 on 2023-01-14 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_postab'),
    ]

    operations = [
        migrations.CreateModel(
            name='sidepost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageside', models.ImageField(upload_to='images')),
                ('dateside', models.TextField()),
                ('headsub', models.TextField()),
            ],
        ),
    ]
