# Generated by Django 5.0 on 2023-12-22 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ultras', '0024_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
            ],
        ),
    ]
