# Generated by Django 5.0 on 2023-12-23 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ultras', '0028_remove_product_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100, unique=True)),
                ('password', models.CharField(default='', max_length=100)),
                ('contact', models.CharField(default='', max_length=10)),
                ('address', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
