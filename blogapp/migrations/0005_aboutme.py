# Generated by Django 4.1.4 on 2023-01-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_postdb_authorname'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('subname', models.CharField(max_length=25)),
                ('myimg', models.ImageField(upload_to='images')),
                ('thumbnail', models.ImageField(upload_to='images')),
            ],
        ),
    ]
